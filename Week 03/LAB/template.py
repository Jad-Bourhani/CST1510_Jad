"""
RECORD CHECK  -  my version
===========================

Name  : Jad Bourhani
Lane  : AI
Date  : 10-10-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).
#
def status_of(percent):
    """Return OVER LIMIT, WARNING or OK for a percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"
 
 
def check(value, limit):
    """Return the difference (limit - value) and value as a percentage of limit."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent
 
 
def print_report(label, value, limit, difference, percent, status):
    """Print the bordered report for one dataset."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Loaded      : {value:>10.2f}")
    print(f"  Expected    : {limit:>10.2f}")
    print(f"  Missing     : {difference:>10.2f}")
    print(f"  Percent     : {percent:>10.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)

over_count = 0
 
while True:


# ==================================================================== INPUT
# 2. Ask for your three values.
#
    label = input("Dataset name (or quit): ")
    if label == "quit":
        break
    value = float(input("Rows loaded: "))
    limit = float(input("Rows expected: "))


# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.
#
    difference, percent = check(value, limit)
    status = status_of(percent)
    if status == "OVER LIMIT":
        over_count += 1


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : call print_report() instead of printing directly here, and
#                wrap sections 2-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# your report lines go here

print("=" * 34)

print_report(label, value, limit, difference, percent, status)
 
print(f"Records over limit this session: {over_count}")


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
