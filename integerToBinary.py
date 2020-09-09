# 4 -> 100
from Stack import Stack

def toBinary(num):
    s = Stack()
    while num > 0:
        rem = num % 2
        s.push(str(rem))
        num = num//2

    res = ""
    while not s.is_empty():
        res += s.pop()
    return res

print toBinary(242)

