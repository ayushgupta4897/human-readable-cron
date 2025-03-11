#!/usr/bin/env python3
"""
Demo script for human-readable-cron.
"""

from human_readable_cron import convert_to_cron

def main():
    """
    Demonstrate the usage of human-readable-cron with interactive input.
    """
    print("Human Readable Cron - Interactive Demo")
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