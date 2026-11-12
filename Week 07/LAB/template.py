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

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

# your function(s) go here
def parse_line(raw_line):
    line = raw_line.strip().lower()
    dataset_part, rest = line.split(",", 1)
    dataset = dataset_part.strip()

    fields = {}
    for piece in rest.split(","):
        key, value = piece.split("=")
        fields[key.strip()] = float(value.strip())

    return {
        "dataset": dataset,
        "rows_loaded": fields["rows_loaded"],
        "rows_expected": fields["rows_expected"],
    }

def status_of(rows_loaded, rows_expected):
    percent = (rows_loaded / rows_expected) * 100
    if percent >= 100:
        return "OK"
    elif percent >= 90:
        return "WARNING"
    else:
        return "FLAGGED"


# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

raw_records = []
with open(r"/Users/jadb/Documents/Documents - MacBook Air/MDX Dubai/CST1510/Week 07/LAB/messy_lines.txt") as f:
    for raw_line in f:
        raw_records.append(raw_line)


# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.
records_checked = 0
flagged_count = 0

for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record["rows_loaded"], record["rows_expected"])

    print(record, "->", status)

    records_checked += 1
    if status == "FLAGGED":
        flagged_count += 1

print()
print(f"{records_checked} records checked, {flagged_count} flagged")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
