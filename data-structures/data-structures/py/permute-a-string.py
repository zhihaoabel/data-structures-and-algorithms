def permutations(input_string):
    """
    :param: input string
    Return - list of all permutations of the input string
    TODO: complete this function to return a list of all permutations of the string
    """
    final_strings = []
    if len(input_string) == 0:
        final_strings.append('')

    else:
        first_character = input_string[0]
        rest_string = input_string[1:]

        sub_strings = permutations(rest_string)
        for sub_string in sub_strings:
            for possible_index in range(len(sub_string) + 1):
                if possible_index == 0:
                    new_string = first_character + sub_string
                else:
                    new_string = sub_string[0:possible_index] + first_character + sub_string[possible_index:]
                final_strings.append(new_string)
    return final_strings


def function_test(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = permutations(string)

    output.sort()
    solution.sort()

    if output == solution:
        print("Pass")
    else:
        print("Fail")


string = 'ab'
solution = ['ab', 'ba']
test_case = [string, solution]
function_test(test_case)

string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
test_case = [string, output]
function_test(test_case)

string = 'abcd'
output = ['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab', 'cdba', 'abdc',
          'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']
test_case = [string, output]
function_test(test_case)
