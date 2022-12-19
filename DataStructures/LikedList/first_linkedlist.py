from typing import Optional


class Node():
    def __init__(self, value, next=None, previous=None) -> None:
        self._value = value
        self._next = next
        self._previous = previous

    @property
    def value(self):
        return self._value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next

    @property
    def previous(self):
        return self._previous

    @previous.setter
    def previous(self, next):
        self._previous = next


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
            node = self.traverse_to_index(index-1)
            new = Node(value=value, next=node.next)
            node.next = new
            self.length += 1

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
        elif index >= self.length:
            parent = self.traverse_to_index(self.length-2)
            self.tail = parent
            self.tail.next = None
        else:
            parent = self.traverse_to_index(index-1)
            parent.next = parent.next.next
        self.length -= 1

    def traverse_to_index(self, index):
        node = self.head
        if index >= self.length:
            index = self.length-1
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

    def reverse(self):
        node = self.head
        self.tail = node
        previous = None
        while node is not None:
            temp = node.next
            node.next = previous
            previous = node
            node = temp
        self.head = previous

    def __repr__(self):
        output = str(self.to_list())
        return output

    def __str__(self):
        output = f"LL(len:{self.length}): "
        node = self.head
        while node is not None:
            output += f"{node.value}-> "
            node = node.next
        output += "None"

        # for i in range()
        # output = str(self.to_list())
        return output

    @staticmethod
    def _print_and_return_next(node):
        print(node.value)
        return node.next


class DoublyLinkedList(LinkedList):
    def __init__(self, value) -> None:
        super().__init__(value)

    def append(self, value):
        new = Node(value=value)
        self.tail.next = new
        new.previous = self.tail
        self.tail = new
        self.length += 1

    def prepend(self, value):
        new = Node(value=value)
        new.next = self.head
        self.head.previous = new
        self.head = new
        self.length += 1

    def insert(self, value, index):
        if index <= 1:
            self.prepend(value)
        elif index >= self.length:
            self.append(value)
        else:
            node = self.traverse_to_index(index-1)
            new = Node(value=value, next=node.next, previous=node)
            node.next = new
            self.length += 1

    def __str__(self):
        output = f"DLL(len:{self.length}): "
        node = self.head
        while node is not None:
            output += f"{node.value} <-> "
            node = node.next
        output += "None"

        # for i in range()
        # output = str(self.to_list())
        return output


ls = LinkedList(1)
ls.append(2)
ls.append(3)
ls.append(4)
ls.prepend(0)
ls.insert(6, 3)
ls.insert(-1, 0)
ls.insert(7, 10)
ls.remove(0)
ls.remove(3)
ls.remove(100)
# ls.remove(4)
print(ls)
ls.reverse()
print(ls)
ls.remove(3)
print(ls)

# dls = DoublyLinkedList(1)
# print(dls)
