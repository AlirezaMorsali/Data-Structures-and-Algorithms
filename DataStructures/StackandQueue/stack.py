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


class Stack_list():
    def __init__(self) -> None:
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop() if len(self.data) > 0 else None

    def peek(self):
        return self.data[-1] if len(self.data) > 0 else None

    def __repr__(self) -> str:
        return f"{self.data}"


class Stack():
    def __init__(self) -> None:
        self.length = 0
        self.top = None
        self.bottom = None

    def push(self, value):
        tmp = Node(value, next=self.top)
        self.top = tmp
        if self.length == 0:
            self.bottom = self.top
        self.length += 1
        # if self.top or self

    def peek(self):
        return self.top.value if self.top else None

    def pop(self):
        if self.top is None:
            return None
        if self.top == self.bottom:
            self.bottom = None
        val = self.top.value
        self.top = self.top.next
        self.length -= 1
        return val

    def __repr__(self) -> str:
        s = ""
        node = self.top
        while node:
            s += f"{node.value}/"
            node = node.next
        return s


# st = Stack()
st = Stack_list()
st.push("googel")
st.push("udemy")
st.push("discord")
print(st)

print(st.pop())
print(st)

print(st.pop())
print(st)

print(st.pop())
print(st)

print(st.pop())
print(st.peek())
print(st)
