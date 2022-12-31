from itertools import zip_longest
"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".


Constraints:

    1 <= s.length, t.length <= 200
    s and t only contain lowercase letters and '#' characters.


Follow up: Can you solve it in O(n) time and O(1) space?
"""


def backspaceCompare(s: str, t: str) -> bool:
    final_s = ""
    final_t = ""
    while "#" in s:
        ind = s.find("#")
        s = s[:ind-1]+s[ind+1:]
    while "#" in t:
        ind = t.find("#")
        t = t[:ind-1]+t[ind+1:]
    return s == t


def eff_backspaceCompare(s: str, t: str) -> bool:
    def get_char(x):
        bs_counter = 0
        for c in reversed(x):
            if c == "#":
                bs_counter += 1
            elif bs_counter > 0:
                bs_counter -= 1
            else:
                yield c

    return all(c1 == c2 for c1, c2 in zip_longest(get_char(s), get_char(t)))


print(f"""
Example 2:
Input: s = "ab##", t = "c#d#"
expected output: true
My result: {eff_backspaceCompare(s = "ab##", t = "c#d#")}
Explanation: Both s and t become""")

# Example 3:

# Input: s="a#c", t="b"
# Output: false
# E
# """
