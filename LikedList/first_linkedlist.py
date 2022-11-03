from typing import Optional


class Node():
    def __init__(self, value, next=None) -> None:
        self._value = value
        self._next = next

    @property
    def value(self):
        return self._value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next


class LinkedList():
    def __init__(self, value) -> None:
        self.head = Node(value=value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new = Node(value=value)
        tmp = self.tail
        tmp.next = new
        self.tail = new
        self.length += 1

    def traverse(self):
        node = self._print_and_return_next(self.head)
        while (node.next is not None):
            node = self._print_and_return_next(node)

    @staticmethod
    def _print_and_return_next(node):
        print(node.value)
        return node.next


ls = LinkedList(1)
ls.append(2)
ls.append(3)
ls.append(4)
ls.traverse()
