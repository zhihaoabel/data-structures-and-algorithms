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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
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

"""
Part A

1. 找出所有由班加罗尔人拨出的电话记录
2. 遍历这些电话记录，找出接听的的电话号码， 并且判断这些电话号码的类型， 过滤掉重复的area code
"""


def get_area_code(number):
    if number.startswith('('):
        return number.split(')')[0][1:]
    elif number.startswith('140'):
        return '140'
    else:
        return number.split(' ')[0][:4]


# test case for get_area_code()
assert get_area_code('(080)67362492') == '080'
assert get_area_code('1409994233') == '140'
assert get_area_code('98453 94494') == '9845'


def is_bangalore(number):
    return number.startswith('(080)')


# test case for is_bangalore()
assert is_bangalore('(080)67362492')


def get_bangalore_calls(calls, pos=0):
    return [call for call in calls if is_bangalore(call[pos])]


# test case for get_bangalore_calls()
assert get_bangalore_calls(calls)[0][0] == '(080)45291968'
assert get_bangalore_calls(calls)[1][0] == '(080)62164823'


def get_area_codes(calls):
    area_codes = set()

    bangalore_calls = get_bangalore_calls(calls, 0)
    for bangalore_call in bangalore_calls:
        area_codes.add(get_area_code(bangalore_call[1]))
    return area_codes


for call in get_area_codes(calls):
    print(call)

"""
Part B

1. 找出所有由班加罗尔人拨出的电话记录
2. 从上述电话记录中找出接听电话号码是班加罗尔的电话记录
3. 计算接听电话是班加罗尔的电话记录占所有由班加罗尔人拨出的电话记录的比例，保留两位小数
"""


def get_bangalore_calls_to_bangalore(calls):
    bangalore_calls = get_bangalore_calls(calls, 0)
    return [call for call in bangalore_calls if is_bangalore(call[1])]


bangalore_calls = get_bangalore_calls(calls)
bangalore_calls_to_bangalore = get_bangalore_calls_to_bangalore(bangalore_calls)
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
    format(len(bangalore_calls_to_bangalore) / len(bangalore_calls) * 100, '.2f')))
