"""
Intro to Python Project 1, Task 1

Complete each task in the file for that task. Submit the whole folder
as a zip file or GitHub repo. 
Full submission instructions are available on the Project Preparation page.
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
TASK 1: 
How many different telephone numbers are there in the records? 
Print a message: 
"There are <count> different telephone numbers in the records."
"""

number_set = set()

for text in texts:
    outbound_number = text[0] 
    inbound_number = text[1] 
    number_set.add(outbound_number)
    number_set.add(inbound_number)
    
for call in calls:
    outbound_number = call[0] 
    inbound_number = call[1] 
    number_set.add(outbound_number)
    number_set.add(inbound_number)

print("There are {} different telephone numbers in the records.".format(len(number_set)))    
