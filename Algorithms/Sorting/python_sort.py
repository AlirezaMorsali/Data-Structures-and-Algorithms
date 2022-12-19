class myint():
    def __init__(self, val) -> None:
        self.val = val

    def __repr__(self) -> str:
        return f"{self.val}"

    def __lt__(self, other):
        return True


a = myint(2)
b = myint(3)
print(a)
print(a > b)
print(a < b)

x = [8, 3, 4, 9, 1, 2, 7]
print(sorted(x))
print(x)
