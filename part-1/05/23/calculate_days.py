"""
 Define a simple nextDay procedure, that assumes
 every month has 30 days.

 For example:
    nextDay(1999, 12, 30) => (2000, 1, 1)
    nextDay(2013, 1, 30) => (2013, 2, 1)
    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
"""


def next_day(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    day += 1

    if day > days_in_month(year, month):
        day = 1
        month += 1

        if month > 12:
            month = 1
            year += 1

    return year, month, day


# test cases for next_day()
# print(next_day(1999, 12, 30))
# print(next_day(2013, 1, 30))
# print(next_day(2012, 12, 30))


def days_between_dates(year1, month1, day1, year2, month2, day2):
    """
    Returns the number of days between year1/month1/day1
    and year2/month2/day2. Assumes inputs are valid dates
    in Gregorian calendar, and the first date is not after
    the second.
   """
    assert (year1, month1, day1) <= (year2, month2, day2), "AssertionError"

    days = 0
    while date_is_before(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = next_day(year1, month1, day1)
        days += 1

    return days


def is_leap_year(year):
    """
    闰年的情况：
    能被400整除
    能被4整除但不能被100整除
    """
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True
    return False


# test cases for is_leap_year()
print(is_leap_year(1992))
print(is_leap_year(2000))
print(is_leap_year(2004))
print(is_leap_year(2003))
print(is_leap_year(1900))
print('test for is_leap_year() passed')


def date_is_before(year1, month1, day1, year2, month2, day2):
    """
    Returns True if year1-month1-day1 is before year2-month2-day2.
   Otherwise, returns False.

    Python tuples are compared lexicographically, comparing the first items first, then the second items,
    and so on. This behavior is exactly what we want when comparing dates.
    """
    return (year1, month1, day1) < (year2, month2, day2)


def days_in_month(year, month):
    month_days = {
        1: 31,  # January
        2: 28,  # February in non-leap year
        3: 31,  # March
        4: 30,  # April
        5: 31,  # May
        6: 30,  # June
        7: 31,  # July
        8: 31,  # August
        9: 30,  # September
        10: 31,  # October
        11: 30,  # November
        12: 31,  # December
    }

    if month == 2 and is_leap_year(year):
        return month_days[month] + 1
    return month_days[month]


# test cases for days_in_month()
print(days_in_month(2000, 2))
print(days_in_month(2003, 2))
print(days_in_month(2023, 4))
print(days_in_month(2023, 8))


# test for days_between_dates()
def test():
    test_cases = [((2012, 9, 30, 2012, 10, 30), 30),
                  ((2012, 1, 1, 2013, 1, 1), 360),
                  ((2012, 9, 1, 2012, 9, 4), 3),
                  ((2013, 1, 1, 1999, 12, 31), "AssertionError")]

    for (args, answer) in test_cases:
        try:
            result = days_between_dates(*args)
            if result != answer:
                print("Test with data:", args, "failed")
            else:
                print("Test case passed!")
        except AssertionError:
            if answer == "AssertionError":
                print("Nice job! Test case {0} correctly raises AssertionError!\n".format(args))
            else:
                print("Check your work! Test case {0} should not raise AssertionError!\n".format(args))


test()

print(days_between_dates(2023, 9, 1, 2023, 9, 16))
print(days_between_dates(2023, 9, 1, 2023, 10, 16))
print(days_between_dates(2000, 1, 1, 2001, 1, 1))
