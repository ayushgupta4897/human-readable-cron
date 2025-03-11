#!/usr/bin/env python3
"""
Example usage of the human-readable-cron library.
"""

from human_readable_cron import convert_to_cron

def main():
    """Demonstrate various examples of human-readable cron conversions."""
    examples = [
        "every Monday at 10 AM",
        "daily at midnight",
        "every hour",
        "every 15 minutes",
        "on the 1st at noon",
        "every weekday at 9 AM",
        "every weekend at 10 AM",
        "every January 1st at midnight",
        "every December 25th at 8 AM",
    ]

    print("Human Readable Cron - Example Conversions")
    print("=" * 50)
    
    for example in examples:
        cron = convert_to_cron(example)
        print(f'"{example}" → "{cron}"')


if __name__ == "__main__":
    main() 