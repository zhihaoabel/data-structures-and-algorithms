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

"""
1. 遍历texts，将所有以140开头且中间没有空格的电话加入到一个set1中。
2. 遍历calls，将所有以140开头且中间没有空格的收听电话也加入到set1中，将所有以140开头且中间没有空格的呼出电话加入到set2。
这样set1中就是所有发送过短信或者收听过短信/电话的销售电话，set2中就是所有呼出过电话的销售电话。
3. 遍历set2，将其中存在set1中的电话号码删除，剩下的就是只呼出过电话，没有发送过短信或者收听过短信/电话的销售电话。
"""


def get_telemarketers(calls, texts):
    outgoing_calls = set([call[0] for call in calls])
    incoming_calls = set([call[1] for call in calls])

    outgoing_texts = set([text[0] for text in texts])
    incoming_texts = set([text[1] for text in texts])

    possible_telemarketers = outgoing_calls - (incoming_calls | outgoing_texts | incoming_texts)
    return sorted(list(possible_telemarketers))


telemarketers = get_telemarketers(calls, texts)
print("These numbers could be telemarketers: ")
for telemarketer in telemarketers:
    print(telemarketer)
