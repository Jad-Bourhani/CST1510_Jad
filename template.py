"""
RECORD CHECK  -  my version
===========================

Name  : JAD
Lane  :  AI
Date  : 27/09/2023

Run it:   python template.py

"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.

label = input("Label: ")
first = float(input("First value: "))
second = float(input("Second value: "))


# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]

difference = first - second
percent = (second / first) * 100

difference = 0.0   # 
percent = 0.0      # 


# =================================================================== OUTPUT
# 3. Print the report.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"Loaded       : {first:>10.2f}")
print(f"Expected     : {second:>10.2f}")
print(f"Difference   : {difference:>+10.2f}")
print(f"Percent      : {percent:>10.2f} %")

print("=" * 34)

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
