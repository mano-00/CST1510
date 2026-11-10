"""
RECORD CHECK  -  my version
===========================

Name  : Chaw Yadanar Htun
Lane  : Cyber
Date  : 9/October/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def check(value, limit):
    """Return the difference and percentage for a value and limit."""
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent


def status_of(percent):
    """Return the status for a percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def print_report(source_ip, failed_logins, total_attempts,
                 difference, failure_percent, status):
    """Print a formatted login report for one source IP."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {source_ip}")
    print("=" * 34)
    print(f"  Failed logins : {failed_logins:>10.2f}")
    print(f"  Total attempts: {total_attempts:>10.2f}")
    print(f"  Difference    : {difference:>+10.2f}")
    print(f"  Failure rate  : {failure_percent:>10.2f} %")
    print(f"  Status        : {status:>10}")
    print("=" * 34)


over_limit_count = 0

while True:
    source_ip = input("Source IP (or quit): ")

    if source_ip == "quit":
        break

    failed_logins = float(input("Failed logins: "))
    total_attempts = float(input("Total attempts: "))

    difference, failure_percent = check(failed_logins, total_attempts)
    status = status_of(failure_percent)

    if status == "OVER LIMIT":
        over_limit_count += 1

    print_report(source_ip, failed_logins, total_attempts,
                 difference, failure_percent, status)

print("OVER LIMIT records:", over_limit_count)
