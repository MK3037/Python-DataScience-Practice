def scoreOfParentheses(s):
    stack=[]
    count=0

    for i in s:
        if i=='(':
            stack.append(count)
            count=0
        else:
            lastcount = stack.pop()
            count = lastcount + max(2 * count, 1)
        print(i)
        print(stack)
        print(count)
    return count
    
s="(()(()))"
print(scoreOfParentheses(s))