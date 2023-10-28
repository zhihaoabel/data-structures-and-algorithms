def is_palindrome(input):
    """
    Return True if input is palindrome, False otherwise.

    Args:
       input(str): input to be checked if it is palindrome
    """

    def reverse(start_index, input_string):
        if start_index >= len(input_string) / 2:
            return True

        is_equal = input_string[start_index] == input_string[len(input_string) - 1 - start_index]
        if is_equal:
            reverse(start_index + 1, input_string)
        else:
            return is_equal
        return True

    if input is None or input == '':
        return True

    index = 0
    return reverse(index, input)


# Test Cases

print("Pass" if (is_palindrome("")) else "Fail")
print("Pass" if (is_palindrome("a")) else "Fail")
print("Pass" if (is_palindrome("madam")) else "Fail")
print("Pass" if (is_palindrome("abba")) else "Fail")
print("Pass" if not (is_palindrome("Udacity")) else "Fail")
