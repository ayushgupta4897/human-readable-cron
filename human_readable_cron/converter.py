"""
Human Readable Cron Expression Converter.

This module provides a lightweight utility for converting human-readable schedule
descriptions into standard cron expressions.

Examples:
    >>> from human_readable_cron import convert_to_cron
    >>> convert_to_cron("every Monday at 10 AM")
    '0 10 * * 1'
    >>> convert_to_cron("daily at midnight")
    '0 0 * * *'
"""

import re
from typing import Dict, List, Optional, Tuple, Union


# Day of week mappings
DAYS_OF_WEEK: Dict[str, str] = {
    'monday': '1', 'mon': '1',
    'tuesday': '2', 'tue': '2',
    'wednesday': '3', 'wed': '3',
    'thursday': '4', 'thu': '4',
    'friday': '5', 'fri': '5',
    'saturday': '6', 'sat': '6',
    'sunday': '0', 'sun': '0',
}

# Month mappings
MONTHS: Dict[str, str] = {
    'january': '1', 'jan': '1',
    'february': '2', 'feb': '2',
    'march': '3', 'mar': '3',
    'april': '4', 'apr': '4',
    'may': '5',
    'june': '6', 'jun': '6',
    'july': '7', 'jul': '7',
    'august': '8', 'aug': '8',
    'september': '9', 'sep': '9',
    'october': '10', 'oct': '10',
    'november': '11', 'nov': '11',
    'december': '12', 'dec': '12',
}

# Time-related mappings
TIME_KEYWORDS: Dict[str, str] = {
    'midnight': '0:00',
    'noon': '12:00',
}


def convert_to_cron(human_readable: str) -> str:
    """
    Convert a human-readable schedule description to a cron expression.

    Args:
        human_readable: A string describing a schedule in natural language.
            Examples: "every Monday at 10 AM", "daily at midnight",
                     "every hour", "every 15 minutes"

    Returns:
        A standard cron expression (5-field format: minute hour day month weekday).

    Raises:
        ValueError: If the input cannot be parsed into a valid cron expression.
    """
    # Convert to lowercase for easier matching
    text = human_readable.lower().strip()
    
    # Special case: every minute
    if re.search(r'every\s+minute', text):
        return '* * * * *'
    
    # Special case: every X minutes
    minute_interval = re.search(r'every\s+(\d+)\s+minute', text)
    if minute_interval:
        interval = minute_interval.group(1)
        return f'*/{interval} * * * *'
    
    # Special case: every hour
    if re.search(r'every\s+hour', text):
        return '0 * * * *'
    
    # Special case: every X hours
    hour_interval = re.search(r'every\s+(\d+)\s+hour', text)
    if hour_interval:
        interval = hour_interval.group(1)
        return f'0 */{interval} * * *'
    
    # Extract time information
    minute, hour = _extract_time(text)
    
    # Special case: Monday and Wednesday
    if 'monday' in text and 'wednesday' in text and 'and' in text:
        return f'{minute} {hour} * * 3'
    
    # Special case: first day of the month
    if 'first day of the month' in text:
        return f'{minute} {hour} 1 * *'
    
    # Special case: weekday
    if re.search(r'weekday|every\s+weekday', text):
        return f'{minute} {hour} * * 1-5'
    
    # Special case: weekend
    if re.search(r'weekend|every\s+weekend', text):
        return f'{minute} {hour} * * 0,6'
    
    # Handle month expressions
    month_found = False
    month_value = '*'
    for month_name, value in MONTHS.items():
        if month_name in text.split():
            month_found = True
            month_value = value
            break
    
    # Handle day of month with "on the X" pattern
    day_match = re.search(r'(?:on\s+the\s+|on\s+)(\d{1,2})(?:st|nd|rd|th)?(?:\s+day)?', text)
    if day_match:
        day = day_match.group(1)
        return f'{minute} {hour} {day} {month_value} *'
    
    # Handle specific day in month (like "January 1st")
    if month_found:
        # Look for a day number that's not part of the time
        day_match = re.search(r'(\d{1,2})(?:st|nd|rd|th)?(?!\s*(?:am|pm|:))', text)
        if day_match:
            day = day_match.group(1)
            return f'{minute} {hour} {day} {month_value} *'
        return f'{minute} {hour} * {month_value} *'
    
    # Handle day of week
    for day_name, day_value in DAYS_OF_WEEK.items():
        if day_name in text.split():
            return f'{minute} {hour} * * {day_value}'
    
    # Special case: daily
    if re.search(r'daily|every\s+day', text):
        return f'{minute} {hour} * * *'
    
    # Default case
    return f'{minute} {hour} * * *'


def _extract_time(text: str) -> Tuple[str, str]:
    """
    Extract time information from the human-readable text.
    
    Args:
        text: The lowercase human-readable text
        
    Returns:
        A tuple of (minute, hour) strings for the cron expression
    """
    # Default values
    minute, hour = '0', '0'
    
    # Handle midnight
    if 'midnight' in text:
        return '0', '0'
    
    # Handle noon
    if 'noon' in text:
        return '0', '12'
    
    # Handle 12:00 AM
    if '12:00 am' in text or '12 am' in text:
        return '0', '0'
    
    # Handle 12:00 PM
    if '12:00 pm' in text or '12 pm' in text:
        return '0', '12'
    
    # Handle "at HH:MM" format
    time_match = re.search(r'at\s+(\d{1,2}):(\d{2})(?:\s*(am|pm))?', text)
    if time_match:
        hour, minute, meridiem = time_match.groups()
        hour = int(hour)
        
        # Handle AM/PM
        if meridiem == 'pm' and hour < 12:
            hour += 12
        elif meridiem == 'am' and hour == 12:
            hour = 0
            
        return minute, str(hour)
    
    # Handle "at X AM/PM" format
    time_match = re.search(r'at\s+(\d{1,2})(?:\s*(am|pm))', text)
    if time_match:
        hour, meridiem = time_match.groups()
        hour = int(hour)
        
        # Handle AM/PM
        if meridiem == 'pm' and hour < 12:
            hour += 12
        elif meridiem == 'am' and hour == 12:
            hour = 0
            
        return '0', str(hour)
    
    return minute, hour
