"""
RECORD CHECK  -  my version
===========================

Name  : Chaw Yadanar Htun
Lane  : Cyber
Date  : 23/October/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
class Record:
    def __init__(self, label, value, limit):
        """Store the source IP, failed logins and total attempts."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return the status based on the failure percentage."""
        percent = (self.value / self.limit) * 100

        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"


def load_records(path):
    """Read login records from a file into Record objects."""
    records = []

    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))

    return records


records = load_records("login_records.txt")
over_limit_count = 0

for record in records:
    status = record.status()

    if status == "OVER LIMIT":
        over_limit_count += 1

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"  Failed logins : {record.value:>10.2f}")
    print(f"  Total attempts: {record.limit:>10.2f}")
    print(f"  Status        : {status:>10}")
    print("=" * 34)

print("OVER LIMIT records:", over_limit_count)
