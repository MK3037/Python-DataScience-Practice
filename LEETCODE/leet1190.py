def reverseParentheses(s):
        stack=[]
        for i in s:
            if i==')':
                temp=[]
                while stack and stack[-1]!='(':
                    temp.append(stack.pop())
                stack.pop()
                stack.extend(temp)
            else:
                stack.append(i)
        return "".join(stack)

s="(ed(et(oc))el)"
print(reverseParentheses(s))