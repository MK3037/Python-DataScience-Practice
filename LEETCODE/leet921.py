def minAddToMakeValid(s):
        stack=[]        
        for i in s:
            if i=='(':
                stack.append('(')
            elif stack and stack[-1]=='(':  # and i=')' hence
                stack.pop()
            else:
                stack.append(')')
        return len(stack)

s="())"
print(minAddToMakeValid(s))