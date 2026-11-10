"""
RECORD CHECK  -  my version
===========================

Name  : Chaw Yadanar Htun
Lane  : Cyber
Date  : 30/October/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("login_records.csv")

df["percent"] = (df["failed_logins"] / df["total_attempts"]) * 100

df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)

print(df[df["status"] != "OK"])

status_counts = df.groupby("status").size()
print(status_counts)

df.to_csv("login_report.csv", index=False)

status_counts.plot(kind="bar")
plt.title("Login records by status")
plt.tight_layout()
plt.savefig("login_status_counts.png")
plt.show()