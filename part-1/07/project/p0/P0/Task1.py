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


def get_unique_numbers(texts, calls):
    """
    Get unique numbers from texts and calls
    """
    numbers = set()
    for text in texts:
        numbers.add(text[0])
        numbers.add(text[1])
    for call in calls:
        numbers.add(call[0])
        numbers.add(call[1])
    return numbers


print("There are {} different telephone numbers in the records.".format(len(get_unique_numbers(texts, calls))))
