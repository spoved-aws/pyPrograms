class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()
        else:
            return None

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack - 1)]
        else:
            return None

    def __str__(self):
        return str(self.stack)

my_stack = Stack()
my_stack.push(3)
print(my_stack)