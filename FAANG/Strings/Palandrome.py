
def isPalandrome(s: str):
    substring = ''.join([c.lower() for c in s if c.isalnum()])
    return substring == substring[::-1]


def almostPalandrome(s: str):
    substring = ''.join([c.lower() for c in s if c.isalnum()])
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            one, two = s[left:right], s[left + 1:right + 1]
            return one == one[::-1] or two == two[::-1]
        left, right = left + 1, right - 1
    return True


# print(isPalandrome(s))
print(almostPalandrome("deeee"))
