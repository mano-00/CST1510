"""
RECORD CHECK  -  my version
===========================

Name  : Chaw Yadanar Htun
Lane  : Cyber
Date  : 6/November/2026

Run it:   python template.py


"""
def parse_line(raw_line):
    """Clean a raw login line and return its fields as a dictionary."""
    line = raw_line.strip().lower()
    fields = {}

    for piece in line.split(","):
        key, value = piece.split("=", 1)
        fields[key.strip()] = value.strip()

    return {
        "src": fields["src"],
        "attempts": int(fields["attempts"]),
        "result": fields["result"]
    }


def status_of(result):
    """Return FLAGGED for a failed login result, otherwise OK."""
    if result == "failed":
        return "FLAGGED"
    else:
        return "OK"


record_count = 0
flagged_count = 0

with open("messy_logins.txt") as f:
    for raw_line in f:
        record = parse_line(raw_line)
        status = status_of(record["result"])

        print(record, status)

        record_count += 1

        if status == "FLAGGED":
            flagged_count += 1

print(f"{record_count} records checked, {flagged_count} flagged")