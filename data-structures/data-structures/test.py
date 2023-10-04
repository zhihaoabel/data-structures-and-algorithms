# class DoubleNode:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#         self.previous = None
#
#
# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def append(self, value):
#         if self.head is None:
#             self.head = DoubleNode(value)
#             self.tail = self.head
#             return
#
#         # 新建结点
#         new_node = DoubleNode(value)
#         # 新结点 previous 指向尾结点
#         new_node.previous = self.tail
#         # 尾结点next指向新结点
#         self.tail.next = new_node
#         # 更新尾结点为新结点
#         self.tail = self.tail.next
#
#
# # Test your class here
#
# linked_list = DoublyLinkedList()
# linked_list.append(1)
# linked_list.append(-2)
# linked_list.append(4)
#
# print("Going forward through the list, should print 1, -2, 4")
# node = linked_list.head
# while node:
#     print(node.value)
#     node = node.next
#
# print("\nGoing backward through the list, should print 4, -2, 1")
# node = linked_list.tail
# while node:
#     print(node.value)
#     node = node.previous


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

    # Define a function outside of the class
    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        node = Node(value)
        node.next = self.head
        self.head = node

    def append(self, value):
        """ Append a value to the end of the list. """
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next

        new_node = Node(value)
        node.next = new_node

    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        if self.head is None:
            return None

        target = self.head
        while True:
            if target.value == value:
                break
            target = target.next
        return target

    def remove(self, value):
        """ Remove first occurrence of value. """
        if self.head is None:
            return

        # 如果头结点就是待删除元素，将头结点后移
        if value == self.head.value:
            self.head = self.head.next
            return

        # 已经处理过删除头结点的情况
        node = self.head
        while node.next:
            if node.next.value == value:
                # 用待删除结点的下一个结点替换待删除结点
                node.next = node.next.next
                return

            node = node.next


# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"

# Test append - 1
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"

# Test append - 2
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

print("Test remove")
# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"
