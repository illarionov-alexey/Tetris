class Stack:

    def __init__(self):
        self.data = []

    def push(self, el):
        self.data.append(el)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return None if self.is_empty() else  self.data[len(self.data)-1]

    def is_empty(self):
        return len(self.data) == 0