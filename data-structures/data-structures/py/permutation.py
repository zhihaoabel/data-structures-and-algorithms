# Code

import copy


def permute(input_list: list):
    """
    Args: myList: list of items to be permuted
    Returns: list of permutation with each permuted item being represented by a list

    定义 compoundList = [[]]
    倒序遍历 inputList, 获得 current_element
        定义 child_lists = [], 用来添加 deep_copy更新后的 list
        得到第一个子 list 长度, 生成索引位置构成的 possible_positions
        遍历 compoundList 中的子 list .
            for循环遍历 possible_positions
                deepcopy 当前子 list, 在 possible_position 位置插入 current_element
                    child_lists 添加该子 list
        compoundList = child_lists
    """
    compound_list = [[]]
    if len(input_list) == 0:
        return compound_list

    if len(input_list) == 1:
        compound_list[0] = input_list
        return compound_list

    for e in input_list[::-1]:
        child_lists = []
        list_length_plus_one = len(compound_list[0]) + 1
        possible_positions = [i for i in range(list_length_plus_one)]
        for child_list in compound_list:
            for index in possible_positions:
                copied_list = copy.deepcopy(child_list)
                copied_list.insert(index, e)
                child_lists.append(copied_list)
        compound_list = child_lists

    return compound_list


# Test Cases

# Helper Function
def check_output(output, expected_output):
    """
    Return True if output and expected_output
    contains the same lists, False otherwise.

    Note that the ordering of the list is not important.

    Examples:
        check_output([ [0, 1], [1, 0] ] ], [ [1, 0], [0, 1] ]) returns True

    Args:
        output(list): list of list
        expected_output(list): list of list

    Returns:
        bool
    """
    o = copy.deepcopy(output)  # so that we don't mutate input
    e = copy.deepcopy(expected_output)  # so that we don't mutate input

    o.sort()
    e.sort()
    return o == e


print("Pass" if (check_output(permute([]), [[]])) else "Fail")
print("Pass" if (check_output(permute([0]), [[0]])) else "Fail")
print("Pass" if (check_output(permute([0, 1]), [[0, 1], [1, 0]])) else "Fail")
print("Pass" if (
    check_output(permute([0, 1, 2]), [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]])) else "Fail")
