from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


def string_rev(s):
    stack = Stack()
    for ch in s:
        stack.push(ch)

    rev_s = ''
    for i in range(stack.size()):
        rev_s += stack.pop()

    return rev_s


print(string_rev('Hello'))
