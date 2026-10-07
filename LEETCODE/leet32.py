def longestValidParentheses(s):
    stack = [-1]
    max_len = 0

    for i, char in enumerate(s):
      if char == "(":
        stack.append(i)
      else:
        stack.pop()
        if not stack:
          stack.append(i)
        else:
          max_len = max(max_len, i - stack[-1])

    return max_len

s="()(()"
print(longestValidParentheses(s))


# def longestValidParentheses(s):
#         ans=[]
#         stack=[]
#         for i in range(len(s)):
#             if s[i]=='(':
#                 stack.append('(')
#             elif stack and s[i]==')':
#                 ans.append(stack.pop())
#                 ans.append(")")
#         return len(ans) 


# s=")()())"
# print(longestValidParentheses(s))