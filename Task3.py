"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

import csv
import re

landline_pattern = re.compile(r'^\((0[0-9]+)\)')

def is_bangalore_number(phone_number):
    """Returns True if number is from bangalore (080)"""
    return phone_number[:5] == '(080)'

def is_landline(phone_number):
    """Returns True if number is a landline (140)"""
    return landline_pattern.match(phone_number) is not None

def is_telemarketer(phone_number):
    """Returns True if number is a telemarketers (140)"""
    return phone_number[:3] == '140'

def is_mobile(phone_number):
    """Returns True if number is mobile"""
    return phone_number[:1] in ['7', '8', '9']

def extract_area_code(phone_number):
    """
    Return the area code if phone number exists, else return an empty string
    """
    if is_telemarketer(phone_number):
        return '140'
    if is_mobile(phone_number):
        return phone_number[:4]
    if is_landline(phone_number):
        return landline_pattern.match(phone_number).group(1)
    return ''

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    sum_from_bang = 0
    sum_to_bang = 0
    area_codes = []

    for call in calls:
        caller, receiver, timestamp, duration = call

        # skip if area code is not recognizable
        area_code = extract_area_code(receiver)
        if not area_code:
            continue

        # skip if caller is not from bangalore
        if not is_bangalore_number(caller):
            continue

        area_codes.append(area_code)
        sum_from_bang += 1

        if is_bangalore_number(receiver):
            sum_to_bang += 1

# Remove duplicates and sort
area_codes = sorted(list(set(area_codes)))

# A:
print('Area odes numbered called by individuals from Bangalore:')
for area_code in area_codes:
    print(area_code)

# B
print(("""{} % of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore.""").format(int((sum_to_bang / sum_from_bang)*100)))
