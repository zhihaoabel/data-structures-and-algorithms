class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return


def iscircular(linked_list):
    """
    Determine whether the Linked List is circular or not
    判断是否存在环形链表的依据：两个指针相遇，且next指针不为空，即均未到达尾结点。
    1. 定义两个结点都从头结点开始循环，慢的每次循环移动一个结点，快的每次移动两个结点
    2. 如果快的结点next为None，说明没有环形结点


    Args:
       linked_list(obj): Linked List to be checked
    Returns:
       bool: Return True if the linked list is circular, return False otherwise
    """
    # 如果只有一个结点或者没有结点，不可能是环形结点
    if linked_list.head is None or linked_list.head.next is None:
        return False

    slow = linked_list.head
    fast = linked_list.head.next

    # 避免空指针
    while fast and fast.next:
        # 快慢两结点在非尾结点相遇。环形链表
        if fast == slow:
            return True
        slow = slow.next
        fast = fast.next.next

    return False


list_with_loop = LinkedList([2, -1, 3, 0, 5])

# Creating a loop where the last node points back to the second node
loop_start = list_with_loop.head.next

node = list_with_loop.head
while node.next:
    node = node.next
node.next = loop_start

# Test Cases

# Create another circular linked list
small_loop = LinkedList([0])
small_loop.head.next = small_loop.head

print("Pass" if iscircular(list_with_loop) else "Fail")  # Pass
print("Pass" if iscircular(LinkedList([-4, 7, 2, 5, -1])) else "Fail")  # Fail
print("Pass" if iscircular(LinkedList([1])) else "Fail")  # Fail
print("Pass" if iscircular(small_loop) else "Fail")  # Pass
print("Pass" if iscircular(LinkedList([])) else "Fail")  # Fail
