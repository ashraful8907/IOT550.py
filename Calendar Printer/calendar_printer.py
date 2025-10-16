days = int(input("How many days in the month?"))
start_day = int(input("What day does the month start on? (0=Sun, 1=Mon, ..., 6=Sat): "))

print("S  M  T  W  T  F  S")
# Add blank spaces for days before the first day
print("  " * start_day, end="")

for day in range(1, days + 1):
    print(f"{day:2}", end = " ")

    if (day + start_day) % 7 == 0:
        print()