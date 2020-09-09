
#{} - Balanced
#[]] - Not balanced

from Stack import Stack

def is_balanced(Paranthesis):
    s = Stack()
    paranDict = {'{': '}', '(': ')', '[': ']'}
    for elem in Paranthesis:
        if elem in paranDict.keys():
            s.push(elem)
        elif elem in paranDict.values() and paranDict[s.peek()] == elem:
            s.pop()

    if s.is_empty():
        return 'Balanced'
    else:
        return 'Not Balanced'

print is_balanced("[{()}]")
print is_balanced("[")
