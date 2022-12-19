def find_first_recurring(x: list):
    s = set()
    for i in x:
        if i in s:
            return i
        else:
            s.add(i)
    return "undefined"


print(find_first_recurring([1,2,3,4,5,6]))