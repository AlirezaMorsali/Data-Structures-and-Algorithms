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
        self.tail.next = new
        self.tail = new
        self.length += 1

    def prepend(self, value):
        new = Node(value=value)
        new.next = self.head
        self.head = new
        self.length += 1

    def insert(self, value, index):
        if index <= 1:
            self.prepend(value)
        elif index >= self.length:
            self.append(value)
        else:
            node = self.traverse_to_index(index)
            new = Node(value=value, next=node.next)
            node.next = new
            self.length += 1

    def traverse_to_index(self, index):
        node = self.head
        for _ in range(index):
            node = node.next
        return node

    def to_list(self):
        vals = []
        node = self.head
        while node is not None:
            vals.append(node.value)
            node = node.next
        return vals

    def __repr__(self):
        output = str(self.to_list())
        return output

    def __str__(self):
        output = str(self.to_list())
        return output

    @staticmethod
    def _print_and_return_next(node):
        print(node.value)
        return node.next


ls = LinkedList(1)
ls.append(2)
ls.append(3)
ls.append(4)
ls.prepend(0)
ls.insert(3.5, 3)
ls.insert(-1, 1)
ls.insert(100, 10)
# ls
print(ls)
