max_size = 6
stack = [0] * max_size
top = -1
isvalid = True

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
        top = top - 1  

n = int(input("How many parentheses would you like to enter (up to 6)? "))

if n > 6:
    print("Maximum allowed is 6. Setting input count to 6.")
    n = 6
elif n%2!=0:
    print("invalid parentheis")

pare = [0] * n 
for i in range(n):
    pare[i] = input(f"Enter value for index {i}: ")


for i in range(len(pare)):
    if pare[i] == "(" or pare[i] == "[" or pare[i] == "{":
        push(pare[i])
    else:
        if top == -1:
            isvalid = False
            break
        
        top2 = stack[top]

        if (pare[i] == ")" and top2 != "(") or (pare[i] == "]" and top2 != "[") or (pare[i] == "}" and top2 != "{"):
            isvalid = False
            break
        pop()

if top != -1:
    isvalid = False

if isvalid:
    print("string is valid")
else:
    print("string isnt valid")