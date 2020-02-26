"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

long_dur = [[int(call_list[3]),call_list[0]] for call_list in calls]
long_dur.sort(key=lambda tup: tup[0],reverse=True)
print(("""{} spent the longest time, {} seconds, on the phone during 
September 2016.""").format(long_dur[0][1],long_dur[0][0]))
