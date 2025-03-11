# Human Readable Cron

[![PyPI version](https://img.shields.io/pypi/v/human-readable-cron.svg)](https://pypi.org/project/human-readable-cron/)
[![Python Versions](https://img.shields.io/pypi/pyversions/human-readable-cron.svg)](https://pypi.org/project/human-readable-cron/)
[![License](https://img.shields.io/github/license/yourusername/human-readable-cron.svg)](https://github.com/yourusername/human-readable-cron/blob/main/LICENSE)

A lightweight utility for converting human-readable schedule descriptions into cron expressions.

## Features

- Zero dependencies - just pure Python
- Simple, intuitive API - just one function call
- Supports a wide range of natural language schedule descriptions
- Comprehensive test coverage
- Lightweight and fast

## Installation

```bash
pip install human-readable-cron
```

## Usage

Using this library is as simple as importing a single function:

```python
from human_readable_cron import convert_to_cron

# Basic usage
cron_expression = convert_to_cron("every Monday at 10 AM")
print(cron_expression)  # Output: 0 10 * * 1
```

### Examples

```python
from human_readable_cron import convert_to_cron

# Days of the week
convert_to_cron("every Monday at 10 AM")      # 0 10 * * 1
convert_to_cron("every Tuesday at 2 PM")      # 0 14 * * 2
convert_to_cron("every Wed at 3:30 PM")       # 30 15 * * 3

# Special times
convert_to_cron("daily at midnight")          # 0 0 * * *
convert_to_cron("daily at noon")              # 0 12 * * *

# Time formats
convert_to_cron("daily at 10:30 AM")          # 30 10 * * *
convert_to_cron("daily at 2:45 PM")           # 45 14 * * *

# Intervals
convert_to_cron("every minute")               # * * * * *
convert_to_cron("every 5 minutes")            # */5 * * * *
convert_to_cron("every hour")                 # 0 * * * *
convert_to_cron("every 2 hours")              # 0 */2 * * *

# Day of month
convert_to_cron("on the 1st at 10 AM")        # 0 10 1 * *
convert_to_cron("on the 15th at 3 PM")        # 0 15 15 * *

# Months
convert_to_cron("every January 1st at noon")  # 0 12 1 1 *
convert_to_cron("every Dec 25 at 8 AM")       # 0 8 25 12 *

# Weekday/Weekend
convert_to_cron("every weekday at 9 AM")      # 0 9 * * 1-5
convert_to_cron("every weekend at 10 AM")     # 0 10 * * 0,6
```

## Supported Formats

The library understands a wide variety of natural language expressions:

- **Days of week**: Monday, Mon, Tuesday, Tue, etc.
- **Times**: 10 AM, 2:30 PM, midnight, noon
- **Intervals**: every minute, every 5 minutes, every hour, every 2 hours
- **Days of month**: on the 1st, on the 15th, on the 31st day
- **Months**: January, Jan, February, Feb, etc.
- **Special periods**: weekday, weekend

## Development

### Setup

```bash
git clone https://github.com/yourusername/human-readable-cron.git
cd human-readable-cron
pip install -e .
pip install -r requirements.txt
```

### Running Tests

```bash
pytest
```

For test coverage:

```bash
pytest --cov=human_readable_cron
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.