from typing import Optional, Any


class my_array():
    def __init__(self, val: Optional[Any] = None) -> None:
        self.length = 0
        self.container = []
        if val is not None:
            self.container.append(val)

    def push(self, val: Optional[Any]):
        self.length += 1
        self.container.append(val)

    def pop(self, index=-1):
        self.length -= 1
        return self.container.pop(index)

    def get(self, index):
        return self.container[index]

    def __str__(self) -> str:
        return f"{self.container}"


ar = my_array()
ar.push(2)
ar.push(3)
ar.push(7)
print(ar)
ar.pop()
print(ar)
ar.pop(0)
print(ar)
