"""
RECORD CHECK  -  my version
===========================

Name  : Jad Bourhani
Lane  :  AI
Date  : 22-10-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

# your class goes here

class Record: 
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit
 
    def percent(self):
        return (self.value / self.limit) * 100
 
    def status(self):
        p = self.percent()
        if p >= 100:
            return "OVER LIMIT"
        elif p >= 90:
            return "WARNING"
        else:
            return "OK"


# ==================================================================== RECORDS
# 2. Create your records.
#
#    Threshold : create at least 2 Record instances directly in the code.
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.

with open('records.txt', 'w') as f:
    f.write('R-001,87,100\n')
    f.write('R-002,120,100\n')
    f.write('R-003,45,100\n')
    f.write('R-004,93,100\n')
    f.write('R-005,101,100')

def load_records(path):
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))
    return records
 
records = load_records("records.txt")


# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    # your report lines go here

over_limit_count = 0
 
for record in records:
    status = record.status()
    percent = record.percent()
 
    if status == "OVER LIMIT":
        over_limit_count += 1
 
    print()
    print("=" * 30)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 30)
    print(f"  Rows loaded   : {record.value:>10f}")
    print(f"  Rows expected : {record.limit:>10f}")
    print(f"  Of expected   : {percent:>8f} %")
    print(f"  Status        : {status:>10}")
    print("=" * 30)
 
print()
print(f"{over_limit_count} of {len(records)} records are OVER LIMIT")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
