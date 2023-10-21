class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


def minimum_bracket_reversals(input_string):
    """
    Calculate the number of reversals to fix the brackets

    Args:
       input_string(string): Strings to be used for bracket reversal calculation
    Returns:
       int: Number of bracket reversals needed

    思路：
    遍历 string。遇到 }，如果栈为空，翻转放入栈中，计数器加一，不为空的话就直接出栈；遇到 {，直接放入栈中
    """
    if input_string is None or len(input_string) == 0:
        return 0

    if len(input_string) % 2 != 0:
        return -1

    count = 0
    stack = Stack()
    for ch in input_string:
        if ch == '}' and stack.is_empty():
            stack.push('{')
            count += 1
        # 不为空直接出栈
        elif ch == '}':
            stack.pop()
        elif ch == '{':
            stack.push('{')

    # 遍历完成后，如果栈不为空，则存满了 {。除以2可以得到这些 { 需要翻转的次数
    if not stack.is_empty():
        average = int(stack.size() / 2)
        count += average
    print(count)
    return count


def function_test(test_case):
    input_string = test_case[0]
    expected_output = test_case[1]
    output = minimum_bracket_reversals(input_string)

    if output == expected_output:
        print("Pass")
    else:
        print("Fail")


test_case_1 = ["}}}}", 2]
function_test(test_case_1)

test_case_2 = ["}}{{", 2]
function_test(test_case_2)

test_case_3 = ["{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}", 13]
function_test(test_case_3)

test_case_4 = ["}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{", 2]
function_test(test_case_4)

test_case_5 = ["}}{}{}{}{}{}{}{}{}{}{}{}{}{}{}", 1]
function_test(test_case_5)
