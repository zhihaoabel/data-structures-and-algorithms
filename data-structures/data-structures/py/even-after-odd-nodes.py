class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def even_after_odd(head):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements

    1. 从头开始遍历结点，用 permutable 记录是否需要置换结点位置，如果结点值为奇数且前面有偶数，调用permutate(node)方法将结点提前
    2. 置换完后重置 permutable。继续从待置换结点往后遍历
    """

    def permutate(head_node, prev_node, permutation_node):
        """
        奇数结点前置

        1. 先看头结点是否是偶数，如果是，直接前插 permutating_node
        2. 从头结点之后开始遍历，当下一个结点值为偶数是，插入 permutating_node
            具体实现：
                a. 将待置换结点的 next 赋给待置换结点上一个节点的 next
                b. 使待置换结点的 next 指向偶数结点
                c. 偶数结点的前一个结点的 next 指向待置换结点
        :param prev_node:
        :param head_node: 更新的头结点
        :param permutation_node: 待移位的结点
        :return:
        """
        if head_node.data % 2 == 0:
            permutation_node.next = head_node
            return

        node = head_node
        while node.next:
            if node.next.data % 2 == 0:
                # 将待置换结点的下一个结点赋给待置换结点的上一个结点的 next
                prev_node.next = permutation_node.next
                # 将待置换结点 next 指向第一个偶数结点
                permutation_node.next = node.next
                # 更新最后一个奇数结点的 next，使其指向待置换结点
                node.next = permutation_node
                return

            node = node.next

    if head is None:
        return

    prev = head
    # 是否需要置换
    permutable = False
    while prev.next:
        current = prev.next
        if prev.next.data % 2 != 0 and permutable:
            permutate(head, prev, current)

            permutable = False
        else:
            # 如果遇到了偶数结点，以后的结点如果遇到奇数就需要置换
            permutable = True
        prev = current

    return head


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
        print(head.data, end=' ')
        head = head.next
    print()


def helper(test_case):
    head = test_case[0]
    solution = test_case[1]

    node_tracker = dict({})
    node_tracker['nodes'] = list()
    temp = head
    while temp:
        node_tracker['nodes'].append(temp)
        temp = temp.next

    head = even_after_odd(head)
    temp = head
    index = 0
    try:
        while temp:
            if temp.data != solution[index] or temp not in node_tracker['nodes']:
                print("Fail")
                return
            temp = temp.next
            index += 1
        print("Pass")
    except Exception as e:
        print("Fail")


arr = [1, 2, 3, 4, 5, 6]
solution = [1, 3, 5, 2, 4, 6]

head = create_linked_list(arr)
test_case = [head, solution]
helper(test_case)

arr = [1, 3, 5, 7]
solution = [1, 3, 5, 7]

head = create_linked_list(arr)
test_case = [head, solution]
helper(test_case)

arr = [2, 4, 6, 8]
solution = [2, 4, 6, 8]
head = create_linked_list(arr)
test_case = [head, solution]
helper(test_case)
