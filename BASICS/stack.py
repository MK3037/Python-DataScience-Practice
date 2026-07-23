max_size = 10
stack = [0] * max_size
top = -1

def push(num):
    global top  
    if top >= max_size - 1:
        print("stack full")
    else:
        top = top + 1
        stack[top] = num

def pop():
    global top  
    if top == -1:
        print("stack empty")
    else:
        print(f"Popped: {stack[top]}")
        top = top - 1  

def display():
    if top == -1:
        print("stack is empty")
    else:
        print("Stack elements:")
        # Loop from top down to 0
        for i in range(top, -1, -1):
            print(stack[i])

push(10)
push(20)
display()
pop()
display()