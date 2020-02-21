"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

num1 = [call_list[0] for call_list in calls]
num2 = [call_list[1] for call_list in calls]
num3 = [call_list[0] for call_list in calls]
num4 = [call_list[1] for call_list in calls]

unique_numbers = list(set(num1+num2+num3+num4))

print(("There are {} different telephone numbers in the records.").format(len(unique_numbers)))