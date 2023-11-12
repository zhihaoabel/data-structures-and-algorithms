class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        """
        This method is used to add an element to the top of the stack.

        Args:
            data: The data to be added to the stack.

        The method works as follows:
        - A new node is created with the provided data.
        - If the stack is empty (i.e., the head is None), the new node becomes the head of the stack.
        - If the stack is not empty, the new node is added to the top of the stack by setting its next pointer to the current head and then updating the head to the new node.
        - The number of elements in the stack is incremented by 1.
        """
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


def reverse_stack(stack):
    """
    Reverse a given input stack

    Args:
       stack(stack): Input stack to be reversed
    Returns:
       stack: Reversed Stack
    """
    # 时间复杂度： O(n)
    # 空间复杂度： O(n)
    tmp = list()
    if stack is None or stack.is_empty():
        return stack

    while not stack.is_empty():
        tmp.append(stack.pop())

    for e in tmp:
        stack.push(e)
    return stack

def function_test(test_case):
    stack = Stack()
    for num in test_case:
        stack.push(num)

    reverse_stack(stack)
    index = 0
    while not stack.is_empty():
        popped = stack.pop()
        if popped != test_case[index]:
            print("Fail")
            return
        else:
            index += 1
    print("Pass")


test_case_1 = [1, 2, 3, 4]
function_test(test_case_1)

test_case_2 = [1]
function_test(test_case_2)
