"""
104. Maximum Depth of Binary Tree
Easy
9.3K
154
Companies

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

"""
from typing import Tuple, List


class Node():
    def __init__(self, value=None, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"value: {self.value}, left: {self.left}, right: {self.right}"

    @staticmethod
    def from_list(lst: List):
        def next_el(i): return lst[i] if i < len(lst) else None
        if len(lst) == 0:
            return Node(None)
        head = Node(next_el(0))
        stack = [head]
        i = 1
        while stack:
            node = stack.pop(0)
            if (left := next_el(i)):
                node.left = Node(left)
                stack.append(node.left)
            i += 1
            if (right := next_el(i)):
                node.right = Node(right)
                stack.append(node.right)
            i += 1

        return head


class BinaryTree():
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)

    def tolist(self):
        return self._tolist(self.root)

    def _tolist(self, node):
        if node is None:
            return []
        else:
            vals = [node.value]
            right = self._tolist(node.right)
            left = self._tolist(node.left)
            right.extend(left)
            vals.extend(right)
            return vals

    def traverse_to_string(self, node):
        if node is None:
            return ""
        else:
            return f"({node.value}): {{right({self.traverse_to_string(node.right)}), left:({self.traverse_to_string(node.left)})}}"

    def breadth_first_search(self):
        def BFS(queue: list, outputs: list):
            if len(queue) == 0:
                return outputs
            else:
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                outputs.append(node.value)
                return BFS(queue, outputs)

        return BFS([self.root], [])

    def traverse_in_order(self, node: Node, traversal: list):
        if node is None:
            return []
        else:
            self.traverse_in_order(node.left, traversal)
            traversal.append(node.value)
            self.traverse_in_order(node.right, traversal)
            return traversal

    def traverse_pre_order(self, node: Node, traversal: list):
        if node is None:
            return []
        else:
            traversal.append(node.value)
            self.traverse_pre_order(node.left, traversal)
            self.traverse_pre_order(node.right, traversal)
            return traversal

    def traverse_post_order(self, node: Node, traversal: list):
        if node is None:
            return []
        else:
            self.traverse_post_order(node.left, traversal)
            self.traverse_post_order(node.right, traversal)
            traversal.append(node.value)
            return traversal

    def __repr__(self) -> str:
        return self.traverse_to_string(self.root)


def maxDepth(root) -> int:
    def depth(node, dep):
        if node is None:
            return dep
        else:
            return depth(node.right, dep+1)
    return depth(root, 0)


x = [3, 9, 20, None, None, 15, 7]
bst = Node.from_list(x)

print(x)
print(bst)
print(maxDepth(bst))
