class Node:
    """LinkedListNode class to be used for this problem"""

    def __init__(self, data):
        self.data = data
        self.next = None


def swap_nodes(head, left_index, right_index):
    """
    :param: head- head of input linked list
    :param: `position_one` - indicates position (index) ONE
    :param: `position_two` - indicates position (index) TWO
    return: head of updated linked list with nodes swapped

    TODO: complete this function and swap nodes present at position_one and position_two
    Do not create a new linked list

    1. 遍历链表，记录 prev1，prev2，left_node，right_node 位置
    2. 当 right_node不为空时，终止循环，开始交换结点位置
    3. 交换思路：
        a. left_tmp 记录 左结点下一个结点
        b. prev2 next指向左结点
        c. 左结点 next指向右结点下一个结点
        d. prev1 next 指向右结点
        e 右结点 next 指向 left_tmp
    """

    def do_swap(prev_left_node, prev_right_node, left, right):
        # 如果左节点紧挨着右结点，左结点同时也是prev2，left_tmp
        if left.next == right:
            left_tmp = left
        else:
            left_tmp = left.next

        # 如果左结点是首结点，prev1 是空
        if prev_left_node is None:
            prev_left_node = Node(None)
            prev_left_node.next = left

        prev_right_node.next = left
        left.next = right.next
        prev_left_node.next = right
        right.next = left_tmp

    if head is None:
        return head

    if left_index < 0 or right_index < 0 or left_index > right_index:
        raise ValueError("索引不正常")

    count = 0
    prev1 = None
    prev2 = None
    left_node = None
    right_node = None
    node = head

    # 确定四个结点的位置
    while node.next:
        if count == left_index - 1:
            prev1 = node
        if count == left_index:
            left_node = node
        if count == right_index - 1:
            prev2 = node
        if count == right_index:
            right_node = node
            break
        count += 1
        node = node.next

    do_swap(prev1, prev2, left_node, right_node)

    # 如果左结点是首结点， 交换后，右结点是首结点
    if prev1 is None:
        head = right_node

    return head


def function_test(test_case):
    head = test_case[0]
    left_index = test_case[1]
    right_index = test_case[2]

    left_node = None
    right_node = None

    temp = head
    index = 0
    try:
        while temp is not None:
            if index == left_index:
                left_node = temp
            if index == right_index:
                right_node = temp
                break
            index += 1
            temp = temp.next

        updated_head = swap_nodes(head, left_index, right_index)

        temp = updated_head
        index = 0
        pass_status = [False, False]

        while temp is not None:
            if index == left_index:
                pass_status[0] = temp is right_node
            if index == right_index:
                pass_status[1] = temp is left_node

            index += 1
            temp = temp.next

        if pass_status[0] and pass_status[1]:
            print("Pass")
        else:
            print("Fail")
        return updated_head
    except Exception as e:
        print("Fail")


# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head


def print_linked_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


arr = [3, 4, 5, 2, 6, 1, 9]
head = create_linked_list(arr)
left_index = 3
right_index = 4
test_case = [head, left_index, right_index]
updated_head = function_test(test_case)

arr = [3, 4, 5, 2, 6, 1, 9]
left_index = 2
right_index = 4
head = create_linked_list(arr)
test_case = [head, left_index, right_index]
updated_head = function_test(test_case)

arr = [3, 4, 5, 2, 6, 1, 9]
left_index = 0
right_index = 1
head = create_linked_list(arr)
test_case = [head, left_index, right_index]
updated_head = function_test(test_case)
