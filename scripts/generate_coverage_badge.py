#!/usr/bin/env python3
"""
Generate a coverage badge for the README.
"""

import re
import subprocess
import sys
from pathlib import Path

def get_coverage():
    """Run pytest with coverage and extract the coverage percentage."""
    result = subprocess.run(
        ["pytest", "--cov=human_readable_cron", "--cov-report=term"],
        capture_output=True,
        text=True,
    )
    
    if result.returncode != 0:
        print("Error running pytest:", result.stderr)
        sys.exit(1)
    
    # Extract coverage percentage from output
    match = re.search(r"TOTAL\s+\d+\s+\d+\s+(\d+)%", result.stdout)
    if not match:
        print("Could not find coverage percentage in output")
        sys.exit(1)
    
    return match.group(1)

def update_readme(coverage):
    """Update the coverage badge in the README."""
    readme_path = Path("README.md")
    if not readme_path.exists():
        print("README.md not found")
        sys.exit(1)
    
    readme_content = readme_path.read_text()
    
    # Update the coverage badge
    new_badge = f"[![Code Coverage](https://img.shields.io/badge/coverage-{coverage}%25-brightgreen.svg)]"
    readme_content = re.sub(
        r"\[\!\[Code Coverage\]\(https://img\.shields\.io/badge/coverage-\d+%25-[a-z]+\.svg\)\]",
        new_badge,
        readme_content
    )
    
    readme_path.write_text(readme_content)
    print(f"Updated README.md with coverage: {coverage}%")

if __name__ == "__main__":
    coverage = get_coverage()
    update_readme(coverage) 