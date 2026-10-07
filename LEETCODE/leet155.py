class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_Stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.min_Stack:
            self.min_Stack.append(value)
        else:
            self.min_Stack.append(min(value, self.min_Stack[-1]))

    def pop(self):
        self.stack.pop()
        self.min_Stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_Stack[-1]


# --- Test Code ---

# 1. Instantiate the object
obj = MinStack()

# 2. Push elements: 3, then 2, then 1
print("Pushing 3, 2, 1...")
obj.push(3)
obj.push(2)
obj.push(1)

# 3. Check current top and current minimum
print("Current Top:", obj.top())      # Expected: 1
print("Current Min:", obj.getMin())   # Expected: 1

# 4. Pop the top element (1)
print("\nPopping top element (1)...")
obj.pop()

# 5. Check top and minimum again after popping
print("Current Top:", obj.top())      # Expected: 2
print("Current Min:", obj.getMin())   # Expected: 2

# 6. Push a larger number (5)
print("\nPushing 5...")
obj.push(5)

# 7. Check top and minimum (minimum should still be 2)
print("Current Top:", obj.top())      # Expected: 5
print("Current Min:", obj.getMin())   # Expected: 2