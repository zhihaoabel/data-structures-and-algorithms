def deep_reverse(arr):
    """
    倒序遍历 arr。
    如果遇到单个元素，直接添加到 list，如果是 list，调用 deep_reverse 递归遍历子 list

    base condition: arr[-1] == output[0]
    :param arr:
    :return:
    """
    final_list = []

    for e in arr[::-1]:
        if isinstance(e, list):
            sub_list = deep_reverse(e)
            final_list.append(sub_list)
        else:
            final_list.append(e)
    return final_list


def function_test(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = deep_reverse(arr)
    if output == solution:
        print("Pass")
    else:
        print("False")


arr = [1, 2, 3, 4, 5]
solution = [5, 4, 3, 2, 1]
test_case = [arr, solution]
function_test(test_case)

arr = [1, 2, [3, 4, 5], 4, 5]
solution = [5, 4, [5, 4, 3], 2, 1]
test_case = [arr, solution]
function_test(test_case)

arr = [1, [2, 3, [4, [5, 6]]]]
solution = [[[[6, 5], 4], 3, 2], 1]
test_case = [arr, solution]
function_test(test_case)

arr = [1, [2, 3], 4, [5, 6]]
solution = [[6, 5], 4, [3, 2], 1]
test_case = [arr, solution]
function_test(test_case)
