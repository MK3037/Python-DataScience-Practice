def minInsertions(s):
        count=0
        stack=[]
        for i in s:
            if i=="(":
                count+=2
                stack.append("(")
                stack.append("(")
                print(count)
            elif i==")" :
                if stack and stack[-1]=="(":
                    count-=1
                    stack.pop()
                elif stack and stack[-1]==")":
                    continue
                else:
                    count+=1
                print(count)
        return count
s="))())("

print(minInsertions(s))