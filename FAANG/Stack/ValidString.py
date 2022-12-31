"""
1249. Minimum Remove to Make Valid Parentheses
Medium
5.5K
103
Companies

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

    It is the empty string, contains only lowercase characters, or
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.

"""


def minRemoveToMakeValid(s: str) -> str:

    stack = []
    st = list(s)
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            if len(stack) == 0:
                st[i] = ""
            else:
                stack.pop()

    for i in stack:
        st[i] = ""

    return "".join(st)
