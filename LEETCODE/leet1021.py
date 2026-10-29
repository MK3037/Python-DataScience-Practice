#how i sloved with fresh mind
def removeOuterParentheses(s):
        stack=[]
        closed=0
        for i in s:
            if i=="(":
                closed+=1               #making sure its not first level bracket
                if closed!=1:
                    stack.append(i)
            else:
                closed-=1
                if closed!=0:
                    stack.append(i)
        return "".join(stack)

s="()()"
print(removeOuterParentheses(s))



#what i tried, ha ha ha
# def removeOuterParentheses(s):
#         stack=[]
#         for i in s:
#             if i=="(":
#                 if stack and stack[-1]==i:
#                     continue
#                 stack.append(i)
#             else:
#                 print(stack)
#                 if stack[-1]==i:
#                     continue
#                 stack.append(i)
#         return "".join(stack)

# s="()()"

# print(removeOuterParentheses(s))