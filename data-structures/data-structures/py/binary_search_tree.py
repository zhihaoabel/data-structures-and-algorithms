import copy
from collections import deque
from typing import Any


class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Queue:
    def __init__(self):
        self.q = deque()

    def enq(self, value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)

    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"


# class Tree:
#     def __init__(self):
#         self.root = None
#
#     def set_root(self, value):
#         self.root = Node(value)
#
#     def get_root(self):
#         return self.root
#
#     def compare(self, node, new_node):
#         """
#         0 means new_node equals node
#         -1 means new node less than existing node
#         1 means new node greater than existing node
#         """
#         if new_node.get_value() == node.get_value():
#             return 0
#         elif new_node.get_value() < node.get_value():
#             return -1
#         else:
#             return 1
#
#     """
#     define insert here
#     can use a for loop (try one or both ways)
#     """
#
#     def insert_with_loop(self, new_value):
#         """
#         根结点直接插入，非根结点则从根结点开始遍历比较
#         如果比较结果 = 0, 替换当前节点
#         如果结果 > 0 且当前节点为叶子节点, 将新节点插入当前结点的右侧，否则更新当前节点为右子节点
#         如果结果 < 0 且当前节点为叶子节点, 将新节点插入当前节点的左侧，否则更新当前结点为左子节点
#
#         :param new_value:
#         :return: None
#         """
#         if self.root is None:
#             self.set_root(new_value)
#             return
#
#         current_node: Node = self.get_root()
#         new_node: Node = Node(new_value)
#         while True:
#             res = self.compare(current_node, new_node)
#             # 当前结点有左子节点，继续DFS
#             if res < 0 and current_node.has_left_child():
#                 current_node = current_node.get_left_child()
#                 continue
#             # 到达左叶子结点
#             elif res < 0 and not current_node.has_left_child():
#                 current_node.set_left_child(new_node)
#                 return
#             # 当前结点有右子结点，继续DFS
#             elif res > 0 and current_node.has_right_child():
#                 current_node = current_node.get_right_child()
#                 continue
#             # 到达右叶子结点
#             elif res > 0 and not current_node.has_right_child():
#                 current_node.set_right_child(new_node)
#                 return
#             # 替换当前节点
#             elif res == 0:
#                 current_node.set_value(new_node.get_value())
#                 return
#
#     """
#     define insert here (can use recursion)
#     try one or both ways
#     """
#
#     def insert_with_recursion(self, value):
#         """
#         递归逻辑：
#             1. 如果比较结果 = 0， 替换当前结点
#             2. 如果比较结果 > 0，
#                 当前结点有右子结点，递归
#                 当前节点没有右子结点，将新节点插入右子结点
#             3. 如果比较结果 < 0，
#                 当前结点有左子结点，递归
#                 当前节点没有左子结点，将新节点插入左子结点
#         :param value:
#         :return:
#         """
#
#         def traverse(current_node: Node):
#             res = self.compare(current_node, new_node)
#             if res == 0:
#                 current_node.set_value(new_node.get_value())
#             elif res == -1:
#                 if current_node.has_left_child():
#                     traverse(current_node.get_left_child())
#                 else:
#                     current_node.set_left_child(new_node)
#             elif res == 1:
#                 if current_node.has_right_child():
#                     traverse(current_node.get_right_child())
#                 else:
#                     current_node.set_right_child(new_node)
#
#         if self.get_root() is None:
#             self.set_root(value)
#             return
#
#         new_node = Node(value)
#
#         traverse(self.get_root())
#
#     """
#     implement search
#     """
#
#     def search(self, value):
#         def traverse(current_node: Node):
#             res = self.compare(current_node, new_node)
#             if res == 0:
#                 return current_node
#             elif res == -1:
#                 if current_node.has_left_child():
#                     return traverse(current_node.get_left_child())
#                 else:
#                     return None
#             elif res == 1:
#                 if current_node.has_right_child():
#                     return traverse(current_node.get_right_child())
#                 else:
#                     return None
#
#         if value is None or self.get_root() is None:
#             return None
#
#         new_node = Node(value)
#         return traverse(self.get_root())
#
#     def __repr__(self):
#         level = 0
#         q = Queue()
#         visit_order = list()
#         node = self.get_root()
#         q.enq((node, level))
#         while (len(q) > 0):
#             node, level = q.deq()
#             if node == None:
#                 visit_order.append(("<empty>", level))
#                 continue
#             visit_order.append((node, level))
#             if node.has_left_child():
#                 q.enq((node.get_left_child(), level + 1))
#             else:
#                 q.enq((None, level + 1))
#
#             if node.has_right_child():
#                 q.enq((node.get_right_child(), level + 1))
#             else:
#                 q.enq((None, level + 1))
#
#         s = "Tree\n"
#         previous_level = -1
#         for i in range(len(visit_order)):
#             node, level = visit_order[i]
#             if level == previous_level:
#                 s += " | " + str(node)
#             else:
#                 s += "\n" + str(node)
#                 previous_level = level
#
#         return s
#
#
# # test case
# tree = Tree()
# tree.insert_with_loop(5)
# tree.insert_with_loop(6)
# tree.insert_with_loop(4)
# tree.insert_with_loop(2)
# tree.insert_with_loop(5)  # insert duplicate
# print(tree)
#
# print(f"""
# search for 8: {tree.search(8)}
# search for 2: {tree.search(2)}
# """)
# print(tree)


class Tree:
    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def compare(self, node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1

    def insert(self, new_value):
        new_node = Node(new_value)
        node = self.get_root()
        if node is None:
            self.root = new_node
            return

        while True:
            comparison = self.compare(node, new_node)
            if comparison == 0:
                # override with new node
                node = new_node
                break  # override node, and stop looping
            elif comparison == -1:
                # go left
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    node.set_left_child(new_node)
                    break  # inserted node, so stop looping
            else:  # comparison == 1
                # go right
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    node.set_right_child(new_node)
                    break  # inserted node, so stop looping

    """
    implement search
    """

    def search(self, value):
        def traverse(current_node: Node):
            res = self.compare(current_node, new_node)
            if res == 0:
                return current_node
            elif res == -1:
                if current_node.has_left_child():
                    return traverse(current_node.get_left_child())
                else:
                    return None
            elif res == 1:
                if current_node.has_right_child():
                    return traverse(current_node.get_right_child())
                else:
                    return None

        if value is None or self.get_root() is None:
            return None

        new_node = Node(value)
        return traverse(self.get_root())

    """
    implement delete
    """

    def delete(self, value):
        """
        DFS遍历 tree。
        如果当前结点的值 < value，往当前节点右子树DFS
        如果当前结点的值 > value，往当前节点左子树DFS
        如果当前结点的值 = value，则删除当前结点，有三种情况：
            1. 当前结点为叶子节点, 则返回 None, 将其父节点指向当前结点的指针设置为 None
            2. 当前结点有一个子节点, 有右子结点则将其父节点的指针指向右子结点, 无则将其父节点的指针指向左子节点
            3. (后继)当前结点有两个子节点, 找出以 当前节点的右子结点为 子BST 的最小左子节点, 将当前结点的值更新为最小左子节点的值.
                按照上述逻辑再次遍历 子DFS, 删除 最小左子节点

        :param value:
        :return:
        """

        def has_child_node(root_node: Node):
            """
            判断当前结点是否有子节点
            :param root_node:
            :return:
            """
            if root_node is None:
                return False
            return True if root_node.has_left_child() or root_node.has_right_child() else False

        def contains_searched_node(root_node: Node, deleting_node: Node):
            """
            比较当前结点的子节点是否包含正在查找的值
            :param deleting_node:
            :param root_node:
            :return:
            """
            if has_child_node(root_node):
                left_node: Node = root_node.get_left_child()
                right_node: Node = root_node.get_right_child()
                # 左/右子节点的值与 val 相等
                if (left_node is not None and left_node.get_value() == deleting_node.get_value()) or (
                        right_node is not None and right_node.get_value() == deleting_node.get_value()):
                    return True
            else:
                # 当前父节点的子节点不包含与 val 相等的子节点
                return False

        def find_parent(root_node: Node, deleting_node: Node):
            """
            DFS 找出子节点值为 val 的 parent_node
            :param deleting_node:
            :param root_node:
            :return:
            """
            # 当前结点的父节点是叶子结点
            if root_node is None:
                return None
            # 当前结点的子节点不满足 val, 且还有子节点
            if not contains_searched_node(root_node, deleting_node):
                res = self.compare(root_node, deleting_node)
                if res == 1:
                    # 往右子树遍历
                    return find_parent(root_node.get_right_child(), deleting_node)
                elif res == -1:
                    # 往左子树遍历
                    return find_parent(root_node.get_left_child(), deleting_node)
            # 找到满足条件的父节点了
            else:
                return root_node

        def get_deleting_node(parent_node: Node, deleting_node: Node):
            """
            根据 parent_node 找到待删除结点
            :param deleting_node:
            :param parent_node:
            :return:
            """
            return parent_node.get_left_child() if parent_node.get_left_child().get_value() == deleting_node.get_value() \
                else parent_node.get_right_child()

        def get_child_node_num(deleting_node: Node):
            """
            判断待删除的结点类型：叶子结点，有一个子节点，有两个子节点
            0：叶子结点
            1：有一个子节点
            2：有两个子节点
            :param deleting_node: 待删除结点
            :return:
            """
            count = 0

            if deleting_node.get_left_child() is not None:
                count += 1
            if deleting_node.get_right_child() is not None:
                count += 1
            return count

        def delete_root_node(root_node: Node):
            """
            删除根结点
            :param root_node: The root node to be deleted
            :return: None
            """
            children_nodes = get_child_node_num(root_node)
            if children_nodes == 0:
                self.set_root(None)
            elif children_nodes == 1:
                self.set_root(root_node.get_left_child().get_value()
                              if root_node.get_left_child() is not None
                              else root_node.get_right_child().get_value())
            else:
                delete_two_child_node(root_node)

        def delete_node(root_node: Node, node_to_delete: Node):
            """
            找到待删除结点的父节点，判断待删除结点的结点类型，根据不同类型进行删除操作
            :param node_to_delete: The node to be deleted
            :param root_node: The root node of the tree
            :return: None
            """
            if root_node is None:
                return

            # If the node to be deleted is the root node
            if root_node.get_value() == node_to_delete.get_value():
                delete_root_node(root_node)
                return

            parent_node = find_parent(root_node, node_to_delete)
            deleting_node = get_deleting_node(parent_node, node_to_delete)

            # Map the number of child nodes to the corresponding deleting function
            delete_func_map = {
                0: delete_leaf_node,
                1: delete_one_child_node,
                2: delete_two_child_node
            }

            # Get the delete function based on the number of child nodes
            delete_func = delete_func_map.get(get_child_node_num(deleting_node))

            # Call the delete function
            delete_func(parent_node, node_to_delete)

        def delete_leaf_node(parent_node: Node, deleting_node: Node):
            """
            将左子节点或者右子结点置为 None
            :param deleting_node:
            :param parent_node:
            :return:
            """
            if parent_node is None:
                return
            if parent_node.get_left_child().get_value() == deleting_node.get_value():
                parent_node.set_left_child(None)
            else:
                parent_node.set_right_child(None)

        def delete_one_child_node(parent_node: Node, deleting_node: Node):
            """
            将parent_node指向待删除结点的指针指向待删除结点的子节点
            :param deleting_node:
            :param parent_node:
            :return:
            """
            # 待删除结点
            left_ptr = None
            right_ptr = None
            # 待删除结点的子节点
            child_node = None
            if parent_node.get_left_child().get_value() == deleting_node.get_value():
                left_ptr = parent_node.get_left_child()
                child_node = left_ptr.get_left_child() if left_ptr.get_left_child() is not None \
                    else left_ptr.get_right_child()
            elif parent_node.get_right_child().get_value == deleting_node.get_value():
                right_ptr = parent_node.get_right_child()
                child_node = right_ptr.get_left_child() if right_ptr.get_left_child() is not None \
                    else right_ptr.get_right_child()

            # 使 parent_node的指针指向 child_node
            if left_ptr is not None:
                parent_node.set_left_child(child_node)
            else:
                parent_node.set_right_child(child_node)

        def find_successor(node: Node) -> Any | None:
            """
            DFS传进来的node找到最左叶子结点
            :param node:
            :return:
            """
            if node is None:
                return node

            successor = node.get_right_child()
            while successor.get_left_child() is not None:
                successor = successor.get_left_child()

            return successor

        def delete_two_child_node(target_node: Node):
            """
            找到后继节点，将后继结点的值赋给待删除的结点
            删除后继结点，因为是后继结点，所以它位于待删除结点的右子树，再次调用 delete_node 方法即可，传入的参数为 待删除结点的右子节点
            :param target_node: 待删除结点
            :return:
            """
            successor = find_successor(target_node)
            successor_copy = copy.deepcopy(successor)
            delete_node(target_node, successor)
            target_node.set_value(successor_copy.get_value())

        if self.get_root() is None:
            return

        if value is None:
            return

        return delete_node(self.get_root(), Node(value))

    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq((node, level))
        while len(q) > 0:
            node, level = q.deq()
            if node is None:
                visit_order.append(("<empty>", level))
                continue
            visit_order.append((node, level))
            if node.has_left_child():
                q.enq((node.get_left_child(), level + 1))
            else:
                q.enq((None, level + 1))

            if node.has_right_child():
                q.enq((node.get_right_child(), level + 1))
            else:
                q.enq((None, level + 1))

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level

        return s


# test cases
tree = Tree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(9)
tree.insert(8)
tree.insert(10)

print(tree)
tree.delete(9)
print(tree)

# # test cases
# tree = Tree()
# tree.insert(5)
# tree.insert(3)
# tree.insert(7)
# tree.insert(2)
# tree.insert(4)
# tree.insert(6)
# tree.insert(9)
# tree.insert(8)
# tree.insert(11)
# tree.insert(10)
#
# print(tree)
# tree.delete(9)
# print(tree)
