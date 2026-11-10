"""
RECORD CHECK  -  my version
===========================

Name  : Chaw Yadanar Htun
Lane  : Cyber 
Date  : 2/October/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

over_limit_count = 0

while True:
    source_ip = input("Source IP (or quit): ")

    if source_ip == "quit":
        break

    failed_logins = float(input("Failed logins: "))
    total_attempts = float(input("Total attempts: "))

    difference = failed_logins - total_attempts
    failure_percent = (failed_logins / total_attempts) * 100

    if failure_percent >= 100:
        status = "OVER LIMIT"
        over_limit_count += 1
    elif failure_percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

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

print("OVER LIMIT records:", over_limit_count)