#Stack DS

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def get_items(self):
        return self.items

    def peek(self):
        return self.items[-1]

s = Stack()
s.push("A")
s.push("B")
print s.get_items()
print s.pop()
print s.is_empty()
print s.peek()
