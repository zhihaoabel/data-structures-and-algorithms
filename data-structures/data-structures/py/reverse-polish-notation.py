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


def evaluate_post_fix(input_list):
    """
    Evaluate the postfix expression to find the answer

    Args:
       input_list(list): List containing the postfix expression
    Returns:
       int: Postfix expression solution
    """

    def calculate_expression(operator, first_operand, second_operand):
        operations = {'/': int.__truediv__,
                      '+': int.__add__,
                      '-': int.__sub__,
                      '*': int.__mul__}

        if operator in operations:
            return operations[operator](int(first_operand), int(second_operand))
        return None

    stack = Stack()
    res = None
    for item in input_list:
        if item == '+' or item == '-' or item == '*' or item == '/':
            if res is None:
                res = stack.pop()
            first = stack.pop()
            res = int(calculate_expression(item, first, res))
            continue

        stack.push(item)

    return res


def function_test(test_case):
    output = evaluate_post_fix(test_case[0])
    print(output)
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")


test_case_1 = [["3", "1", "+", "4", "*"], 16]
function_test(test_case_1)

test_case_2 = [["4", "13", "5", "/", "+"], 6]
function_test(test_case_2)

test_case_3 = [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22]
function_test(test_case_3)
