"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

phone_nums = []

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    for text in list(reader):
        phone_nums.extend(text[:2])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    for call in list(reader):
        phone_nums.extend(call[:2])


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

phone_nums = list(set(phone_nums))

print(("There are {} different telephone numbers in the records.").format(len(phone_nums)))
