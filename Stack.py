class Stack():
    def __init_(self):
        self.stack = []
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        raise IndexError
    def push(self, item):
        self.stack.append(item)
    def isEmpty(self):
        return len(self.stack) == 0
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        raise IndexError
    def __str__(self):
        return str(self.stack)