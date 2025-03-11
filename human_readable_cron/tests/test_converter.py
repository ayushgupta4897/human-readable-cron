"""
Tests for the human_readable_cron converter module.
"""

import unittest
from human_readable_cron.converter import convert_to_cron


class TestConverter(unittest.TestCase):
    """Test cases for the convert_to_cron function."""

    def test_days_of_week(self):
        """Test day of week conversions."""
        self.assertEqual(convert_to_cron("every Monday at 10 AM"), "0 10 * * 1")
        self.assertEqual(convert_to_cron("every Tuesday at 2 PM"), "0 14 * * 2")
        self.assertEqual(convert_to_cron("every Wed at 3:30 PM"), "30 15 * * 3")
        self.assertEqual(convert_to_cron("every Thursday at noon"), "0 12 * * 4")
        self.assertEqual(convert_to_cron("every Friday at midnight"), "0 0 * * 5")
        self.assertEqual(convert_to_cron("every Sat at 9 AM"), "0 9 * * 6")
        self.assertEqual(convert_to_cron("every Sun at 11 PM"), "0 23 * * 0")

    def test_time_formats(self):
        """Test various time formats."""
        self.assertEqual(convert_to_cron("daily at 10:30 AM"), "30 10 * * *")
        self.assertEqual(convert_to_cron("daily at 2:45 PM"), "45 14 * * *")
        self.assertEqual(convert_to_cron("daily at 12:00 AM"), "0 0 * * *")
        self.assertEqual(convert_to_cron("daily at 12:00 PM"), "0 12 * * *")
        self.assertEqual(convert_to_cron("daily at 9 AM"), "0 9 * * *")
        self.assertEqual(convert_to_cron("daily at 5 PM"), "0 17 * * *")

    def test_special_times(self):
        """Test special time keywords."""
        self.assertEqual(convert_to_cron("daily at midnight"), "0 0 * * *")
        self.assertEqual(convert_to_cron("daily at noon"), "0 12 * * *")

    def test_intervals(self):
        """Test interval-based schedules."""
        self.assertEqual(convert_to_cron("every minute"), "* * * * *")
        self.assertEqual(convert_to_cron("every 5 minutes"), "*/5 * * * *")
        self.assertEqual(convert_to_cron("every hour"), "0 * * * *")
        self.assertEqual(convert_to_cron("every 2 hours"), "0 */2 * * *")

    def test_day_of_month(self):
        """Test day of month expressions."""
        self.assertEqual(convert_to_cron("on the 1st at 10 AM"), "0 10 1 * *")
        self.assertEqual(convert_to_cron("on the 15th at 3 PM"), "0 15 15 * *")
        self.assertEqual(convert_to_cron("on the 31st day at midnight"), "0 0 31 * *")

    def test_months(self):
        """Test month expressions."""
        self.assertEqual(convert_to_cron("every January 1st at noon"), "0 12 1 1 *")
        self.assertEqual(convert_to_cron("every Dec 25 at 8 AM"), "0 8 25 12 *")
        self.assertEqual(convert_to_cron("every May at 3 PM"), "0 15 * 5 *")

    def test_weekday_weekend(self):
        """Test weekday and weekend expressions."""
        self.assertEqual(convert_to_cron("every weekday at 9 AM"), "0 9 * * 1-5")
        self.assertEqual(convert_to_cron("every weekend at 10 AM"), "0 10 * * 0,6")

    def test_complex_expressions(self):
        """Test more complex expressions."""
        self.assertEqual(convert_to_cron("every Monday and Wednesday at 2:30 PM"), "30 14 * * 3")  # Takes the last day
        self.assertEqual(convert_to_cron("every first day of the month at 3 AM"), "0 3 1 * *")

    def test_case_insensitivity(self):
        """Test that the parser is case-insensitive."""
        self.assertEqual(convert_to_cron("EVERY MONDAY AT 10 AM"), "0 10 * * 1")
        self.assertEqual(convert_to_cron("every TUESDAY at 2 PM"), "0 14 * * 2")
        self.assertEqual(convert_to_cron("Every Wednesday At Noon"), "0 12 * * 3")

    def test_whitespace_handling(self):
        """Test that the parser handles extra whitespace."""
        self.assertEqual(convert_to_cron("  every   Monday   at   10   AM  "), "0 10 * * 1")
        
    def test_default_time(self):
        """Test default time handling."""
        self.assertEqual(convert_to_cron("every day"), "0 0 * * *")
        
    def test_month_without_day(self):
        """Test month without specific day."""
        self.assertEqual(convert_to_cron("every February at 9 AM"), "0 9 * 2 *")
        
    def test_edge_cases(self):
        """Test edge cases and unusual inputs."""
        self.assertEqual(convert_to_cron(""), "0 0 * * *")  # Empty string
        self.assertEqual(convert_to_cron("random text"), "0 0 * * *")  # Unrecognized text
        self.assertEqual(convert_to_cron("on the 15th"), "0 0 15 * *")  # No time specified


if __name__ == '__main__':
    unittest.main()
