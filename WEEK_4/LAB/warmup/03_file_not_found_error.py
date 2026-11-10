with open("records.txt", "w") as f:
    f.write("R-001,87,100\n")

with open("records.txt") as f:
    print(f.read())