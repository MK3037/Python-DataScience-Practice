class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item from the stack."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(f"Stack size: {stack.size()}")       
print(f"Top element (peek): {stack.peek()}") 

print(f"Popped element: {stack.pop()}")   
print(f"New top element: {stack.peek()}") 
print(f"Is stack empty? {stack.is_empty()}") 