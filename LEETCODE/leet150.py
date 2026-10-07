def evalRPN(tokens):
        stack = []
        for i in tokens:
            if i == '+':
                stack.append(stack.pop() + stack.pop())
            elif i == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif i == '*':
                stack.append(stack.pop() * stack.pop())
            elif i == '/':
                b = stack.pop()
                a = stack.pop()
                # int(a / b) truncates towards zero in Python 3
                stack.append(int(a / b))
            else:
                stack.append(int(i))
                
        return stack[0]

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))