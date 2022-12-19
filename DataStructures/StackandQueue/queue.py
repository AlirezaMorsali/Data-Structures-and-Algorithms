class Node():
    def __init__(self, value, next=None, previous=None) -> None:
        self.value = value
        self.next = next
        self.previous = previous


class Queue():
    def __init__(self) -> None:
        self.length = 0
        self.first = None
        self.last = None

    def enqueue(self, value):
        tmp = Node(value)
        if self.length == 0:
            self.first = self.last = tmp
        else:
            self.last.next = tmp
            self.last = tmp
        self.length += 1
        # if self.top or self

    def peek(self):
        return self.first.value if self.first else None

    def dequeue(self):
        if self.first is None:
            return None
        if self.first == self.last:
            self.bottom = None
        val = self.first.value
        self.first = self.first.next
        self.length -= 1
        return val

    def __repr__(self) -> str:
        s = ""
        node = self.first
        while node:
            s += f"{node.value}/"
            node = node.next
        return s


qu = Queue()
qu.enqueue("john")
print(qu)
qu.enqueue("marry")
print(qu)
qu.enqueue("alex")
print(qu)

print(qu.peek())
print(qu.dequeue())
print(qu)

print(qu.dequeue())
print(qu)

print(qu.dequeue())
print(qu)
print(qu.dequeue())
print(qu)
