# Helper code

# A class behaves like a data-type, just like an int, float or any other built-in ones.
# User defined class
class Node:
    def __init__(self, value):  # <-- For simple LinkedList, "value" argument will be an int, whereas,
        # for NestedLinkedList, "value" will be a LinkedList
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


# User defined class
class LinkedList:
    def __init__(self, head):  # <-- Expects "head" to be a Node made up of an int or LinkedList
        self.head = head

    '''
    For creating a simple LinkedList, we will pass an integer as the "value" argument
    For creating a nested LinkedList, we will pass a LinkedList as the "value" argument
    '''

    def append(self, value):

        # If LinkedList is empty
        if self.head is None:
            self.head = Node(value)
            return

        # Create a temporary Node object
        node = self.head

        # Iterate till the end of the current LinkedList
        while node.next is not None:
            node = node.next

        # Append the newly created Node at the end of the current LinkedList
        node.next = Node(value)

    '''We will need this function to convert a LinkedList object into a Python list of integers'''

    def to_list(self):
        out = []  # <-- Declare a Python list
        node = self.head  # <-- Create a temporary Node object

        while node:  # <-- Iterate until we have nodes available
            out.append(int(str(
                node.value)))  # <-- node.value is actually of type Node, therefore convert it into int before
            # appending to the Python list
            node = node.next

        return out


def sort_linked_list(llist: list) -> LinkedList:
    out = LinkedList(None)
    if llist is None:
        return out

    sorted_list = sorted(llist)
    for e in sorted_list:
        out.append(e)

    return out


def merge(list1: LinkedList | None, list2: LinkedList | None) -> LinkedList:
    """
    The arguments list1, list2 must be of type LinkedList.
    The merge() function must return an instance of LinkedList.
    """
    if list1 is None:
        list1 = LinkedList(None)
    if list2 is None:
        list2 = LinkedList(None)

    merged_list = list1.to_list() + list2.to_list()
    return sort_linked_list(merged_list)


class NestedLinkedList(LinkedList):
    """
    Note: NestedLinkedList每个结点的value是一个LinkedList

    1. 依次遍历 NestedLinkedList 每个结点
    2. 取出结点的value值，即为 LinkedList，递归合并 LinkedList
    3. NestedLinkedList 结点后移
    """

    def flatten(self):
        if self.head is None:
            return NestedLinkedList(None)

        current: Node = self.head
        merged_linked_list = None
        while current:
            # 当前 NestedLinkedList 结点内的 LinkedList
            inner_linked_list: LinkedList = current.value
            merged_linked_list = merge(merged_linked_list, inner_linked_list)
            # 下一个 NestedLinkedList 结点
            current = current.next

        return merged_linked_list

    def flatten2(self):
        """
        递归的写法
        :return:
        """
        return self._flatten(self.head)  # <-- self.head is a node for NestedLinkedList

    '''  A recursive function '''

    def _flatten(self, node):

        # A termination condition
        if node.next is None:
            return merge(node.value, None)  # <-- First argument is a simple LinkedList

        # _flatten() is calling itself untill a termination condition is achieved
        return merge(node.value, self._flatten(node.next))  # <-- Both arguments are a simple LinkedList each


''' Test merge() function'''
linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

merged = merge(linked_list, second_linked_list)
node = merged.head
while node is not None:
    # This will print 1 2 3 4 5
    print(node.value)
    node = node.next

# Lets make sure it works with a None list
merged = merge(None, linked_list)
node = merged.head
while node is not None:
    # This will print 1 3 5
    print(node.value)
    node = node.next

# First Test scenario
''' Create a simple LinkedList'''
linked_list = LinkedList(Node(1))  # <-- Notice that we are passing a Node made up of an integer
linked_list.append(3)  # <-- Notice that we are passing a numerical value as an argument in the append() function here
linked_list.append(5)

''' Create another simple LinkedList'''
second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

''' Create a NESTED LinkedList, where each node will be a simple LinkedList in itself'''
nested_linked_list = NestedLinkedList(
    Node(linked_list))  # <-- Notice that we are passing a Node made up of a simple LinkedList object
nested_linked_list.append(
    second_linked_list)  # <-- Notice that we are passing a LinkedList object in the append() function here

solution = nested_linked_list.flatten()  # <-- returns A LinkedList object

expected_list = [1, 2, 3, 4, 5]  # <-- Python list

# Convert the "solution" into a Python list and compare with another Python list
assert solution.to_list() == expected_list, f"list contents: {solution.to_list()}"
