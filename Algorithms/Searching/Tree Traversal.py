from typing import Optional, Union, Tuple
import sys


class Node():
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"value: {self.value}, left: {self.left}, right: {self.right}"


class BinarySearchTree():
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            node = self._lookup(self.root, value)
            if node.value < value:
                node.right = Node(value)
            elif node.value > value:
                node.left = Node(value)
            else:
                print("Already exists")
                return

    def lookup(self, value):
        node = self._lookup(
            self.root, value) if self.root is not None else None
        if node is None or node.value != value:
            return False
        else:
            return node

    def _parent_lookup(self, node: Node, value) -> Tuple[Node, str]:
        if (left := node.left) is not None and left.value == value:
            return (node, "left")
        elif (right := node.right) is not None and right.value == value:
            return (node, "right")
        else:
            if node.value < value:
                if right is None:
                    print(f"Node with value: {value} does not exist")
                else:
                    return self._parent_lookup(right, value)
            else:
                if right is None:
                    print(f"Node with value: {value} does not exist")
                else:
                    return self._parent_lookup(right, value)

    def _lookup(self, node: Node, value) -> Node:
        if node.value < value:
            return self._lookup(node.right, value) if node.right else node
        else:
            return self._lookup(node.left, value) if node.left else node

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

    def remove(self, value):
        if self.root is None:
            return None
        elif self.root.value == value:
            self.root = None
        else:
            parent, side = self._parent_lookup(self.root, value)
            if side == "right":
                vals = self._tolist(parent.right)[1:]
                parent.right = None
            else:
                vals = self._tolist(parent.left)[1:]
                parent.left = None
            for val in vals:
                self.insert(val)

    def __repr__(self) -> str:
        return self.traverse_to_string(self.root)


class BinaryTree(BinarySearchTree):
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
            return
        else:
            self.traverse_in_order(node.left, traversal)
            traversal.append(node.value)
            self.traverse_in_order(node.right, traversal)
            return traversal

    def traverse_pre_order(self, node: Node, traversal: list):
        if node is None:
            return
        else:
            traversal.append(node.value)
            self.traverse_pre_order(node.left, traversal)
            self.traverse_pre_order(node.right, traversal)
            return traversal

    def traverse_post_order(self, node: Node, traversal: list):
        if node is None:
            return
        else:
            self.traverse_post_order(node.left, traversal)
            self.traverse_post_order(node.right, traversal)
            traversal.append(node.value)
            return traversal

    def __repr__(self) -> str:
        return self.traverse_to_string(self.root)
        # return f"{self.breadth_first_search()}"


bst = BinaryTree()
bst.insert(9)

bst.insert(4)
bst.insert(1)
bst.insert(6)
bst.insert(20)
bst.insert(170)
bst.insert(15)
# bst.insert(0)
# bst.insert(2)
# bst.insert(5)
# bst.insert(7)
# bst.insert(14)
# bst.insert(16)
# bst.insert(150)
# bst.insert(180)


print(bst)
print(f"{bst.breadth_first_search()}")
print(bst.traverse_post_order(bst.root, []))
print(bst.traverse_pre_order(bst.root, []))
print(bst.traverse_in_order(bst.root, []))
