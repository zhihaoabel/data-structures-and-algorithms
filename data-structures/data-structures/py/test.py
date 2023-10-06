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

    def pop(self):
        """ Return the first node's value and remove it from the list. """
        """
        1. 保存头结点的值
        2. 将下一个结点赋值给头结点
        """
        if self.head is None:
            return None

        val = self.head.value
        self.head = self.head.next

        return val

    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
        length of the list, append to the end of the list. """
        """
        1. 插入到头结点位置直接调用prepend方法
        2. 遍历结点并计数。如果索引位置相等，插入结点
        3. 遍历到尾结点仍未到达指定索引位置，放入末尾
        """
        if pos < 0:
            return

        # 头结点插入
        if pos == 0:
            self.prepend(value)
            return

        counter = 0
        node = self.head
        while node.next:
            counter += 1
            if pos == counter:
                new_node = Node(value)

                prev_node = node
                next_node = node.next
                new_node.next = next_node
                prev_node.next = new_node
                return

            node = node.next

        # 遍历到尾结点仍未到达索引位置
        if node.next is None:
            node.next = Node(value)


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

# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

print("Test insert")
# Test insert
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
