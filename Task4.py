"""
Intro to Python Lab 1, Task 4

Complete each task in the file for that task. Submit the whole folder
as a zip file or GitHub repo. 
Full submission instructions are available on the Lab Preparation page.
"""

"""
Read file into texts and calls. 
It's ok if you don't understand how to read files
You will learn more about reading files in future lesson
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

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

inboundcall_and_text_list = []
outboundcall_list = []

for call in calls:
    outboundcall_numbers = call[0]
    inboundcall_numbers = call[1]
    outboundcall_list.append(outboundcall_numbers)
    inboundcall_and_text_list.append(inboundcall_numbers)
for text in texts:
    text_numbers_send = text[0]
    text_numbers_receive = text[1]
    inboundcall_and_text_list.append(text_numbers_send)
    inboundcall_and_text_list.append(text_numbers_receive)

result = []

for outboundcall in outboundcall_list:
    if outboundcall not in inboundcall_and_text_list:
        result.append(outboundcall)

print("These numbers could be telemarketers: \n" + "\n".join(sorted(set(result))))



