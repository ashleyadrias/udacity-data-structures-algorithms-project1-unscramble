"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

import csv

callers = []
whitelist = []

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    for text in list(reader):
        sender, receiver, timestamp = text
        whitelist.extend([sender, receiver])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    for call in list(reader):
        caller, receiver, timestamp, seconds = call
        callers.append(caller)
        whitelist.append(receiver)

# Remove duplicates
callers = list(set(callers))
whitelist = list(set(whitelist))

# Potential telemarketers are numbers that appear in the callers list, but not in the whitelist
suspect_tele = set(callers).difference(whitelist)

print("Potential telemarketers:")
for nums in sorted(suspect_tele):
    print(nums)
