"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
import csv
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    sum = {}

    for call in list(reader):
            caller, receiver, timestamp, duration = call
            duration = int(duration)

            sum[caller] = sum[caller] + duration if caller in sum else duration
            sum[receiver] = sum[receiver] + duration if receiver in sum else duration

# Telephone number(the key) of the longest duration
phone_number = max(sum.keys(), key=(lambda k: sum[k]))

print(("""{} spent the longest time, {} seconds, on the phone during
September 2016.""").format(phone_number,sum[phone_number]))
