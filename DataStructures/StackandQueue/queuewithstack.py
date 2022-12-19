class Stack():
    def __init__(self) -> None:
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop() if len(self.data) > 0 else None

    def peek(self):
        return self.data[-1] if len(self.data) > 0 else None

    def __len__(self):
        return len(self.data)

    def __repr__(self) -> str:
        return f"{self.data}"


class Queue():
    def __init__(self) -> None:
        self.input = Stack()
        self.output = Stack()

    def enqueue(self, value):
        self.input.push(value)

    def dequeue(self):
        if len(self.output) == 0:
            self._update_output()

        return self.output.pop()

    def peek(self):
        if len(self.output) == 0:
            self._update_output()
        return self.output.peek()

    def _update_output(self):
        while (len(self.input) > 0):
            self.output.push(self.input.pop())

    def empty(self):
        if (len(self.input) == 0) and (len(self.output) == 0):
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"{self.input}, {self.output}"


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

qu.enqueue("will")
print(qu)

print(qu.peek())
print(qu.dequeue())
print(qu)

print(qu.dequeue())
print(qu)

print(qu.dequeue())
print(qu)
