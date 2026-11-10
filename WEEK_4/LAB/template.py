"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def load_records(path):
    """Read login records from a file into a list of dictionaries."""
    records = []

    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append({
                "label": label,
                "value": float(value),
                "limit": float(limit)
            })

    return records


def check_record(value, limit):
    """Return the difference, percentage and status for a record."""
    difference = value - limit
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status


def print_report(record, difference, percent, status):
    """Print a formatted report for one login record."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record['label']}")
    print("=" * 34)
    print(f"  Failed logins : {record['value']:>10.2f}")
    print(f"  Total attempts: {record['limit']:>10.2f}")
    print(f"  Difference    : {difference:>+10.2f}")
    print(f"  Failure rate  : {percent:>10.2f} %")
    print(f"  Status        : {status:>10}")
    print("=" * 34)


try:
    records = load_records("login_records.txt")
except FileNotFoundError:
    print("login_records.txt not found.")
    records = []

over_limit_count = 0

with open("login_results.txt", "w") as f:
    for record in records:
        difference, percent, status = check_record(
            record["value"], record["limit"]
        )

        print_report(record, difference, percent, status)
        f.write(f"{record['label']},{status}\n")

        if status == "OVER LIMIT":
            over_limit_count += 1

print("OVER LIMIT records:", over_limit_count)