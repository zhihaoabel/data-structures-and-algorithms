# Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

# write your code here
# HINT: You can use the modulo operator to find a factor

"""
1. 遍历check_prime， 取当前数字的平方根，然后从2开始遍历到平方根，如果能被整除，就不是质数，否则就是质数。
"""


def get_square_root(num):
    """
    This method calculates and returns the square root of a given number.

    :param num: The number for which square root needs to be calculated.
    :return: The square root of the given number.

    """
    return int(num ** 0.5)


def find_factor(square_root, num):
    """

    Find Factor

    Parameters:
        square_root (int): The square root of the number to be checked for factors.
        num (int): The number for which factors are to be found.

    Returns:
        int: The first factor found in the range from 2 to the square root of the number.
             If no factor is found, -1 is returned.

    """
    for i in range(2, square_root + 1):
        if num % i == 0:
            return i
    return -1


def is_prime(n):
    if n <= 1:
        return False
    square_root = get_square_root(n)
    factor = find_factor(square_root, n)
    return factor == -1, factor


for num in check_prime:
    result, factor = is_prime(num)
    if result:
        print("{} is a prime number".format(num))
    else:
        print("{} is not a prime number, because {} is a factor of {}"
              .format(num, factor, num))
