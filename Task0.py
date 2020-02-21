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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

first = 1
last = -1
incoming_num = texts[first][0]
ans_num = texts[first][1]
text_time = texts[first][2]

print(("First record of texts, {} texts {} at time {}").format(incoming_num,ans_num,text_time))

incoming_num = calls[last][0]
ans_num = calls[last][1]
text_time = calls[last][2]
duration = calls[last][3]

print(("Last record of calls, {} calls {} at time {}, lasting {} seconds").format(incoming_num,ans_num,text_time,duration))