#!/usr/bin/env python3
"""
Command-line interface for human-readable-cron.
"""

import argparse
import sys
from human_readable_cron import convert_to_cron, __version__

def main():
    """
    Main entry point for the command-line interface.
    """
    parser = argparse.ArgumentParser(
        description="Convert human-readable schedules to cron expressions."
    )
    parser.add_argument(
        "schedule",
        nargs="?",
        help="Human-readable schedule to convert (e.g., 'every Monday at 10 AM')"
    )
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"human-readable-cron {__version__}"
    )
    parser.add_argument(
        "-i", "--interactive",
        action="store_true",
        help="Run in interactive mode"
    )
    
    args = parser.parse_args()
    
    if args.interactive:
        run_interactive()
    elif args.schedule:
        try:
            cron_expression = convert_to_cron(args.schedule)
            print(cron_expression)
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        parser.print_help()

def run_interactive():
    """
    Run the CLI in interactive mode.
    """
    print("Human Readable Cron - Interactive Mode")
    print("=" * 50)
    print("Type 'exit' to quit")
    print()
    
    while True:
        try:
            human_readable = input("Enter a human-readable schedule: ")
            if human_readable.lower() in ('exit', 'quit', 'q'):
                break
                
            cron_expression = convert_to_cron(human_readable)
            print(f"Cron expression: {cron_expression}")
            print()
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Error: {e}")
    
    print("Thank you for using human-readable-cron!")

if __name__ == "__main__":
    main() 