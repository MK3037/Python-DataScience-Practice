def backspaceCompare(s, t):
        def stackmaker(r):
            stack=[]
            for i in range(len(r)):
                if stack and r[i]=='#':
                    stack.pop()
                elif r[i]!='#':
                    stack.append(r[i])
            return stack
        if stackmaker(s)==stackmaker(t):
            return True
        print(stackmaker(s))
        print(stackmaker(t))
        return False

s = "ab#c"
t = "ad#c"
print(backspaceCompare(s,t))

s="y#fo##f"
t="y#f#o##f"
print(backspaceCompare(s,t))