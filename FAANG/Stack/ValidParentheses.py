"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

"""


def isValidn2(s: str) -> bool:
    stack = []
    valid = {')': '(', '}': '{', ']': '['}
    for c in s:
        if c in valid.values():
            stack.append(c)
        else:
            if len(stack) == 0 or valid[c] != stack.pop():
                return False

    if len(stack) == 0:
        return True
    else:
        return False


def isValid(s: str) -> bool:
    stack = []
    valid = {')': '(', '}': '{', ']': '['}
    for c in s:
        if c in valid.values():
            stack.append(c)
        else:
            if valid[c] != stack.pop():
                return False

    if len(stack) == 0:
        return True
    else:
        return False


print(isValid(""))
print(isValid("()"))
print(isValid("([]{[]}){[]}"))
