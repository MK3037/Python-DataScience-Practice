'''Write a function to find the longest common prefix string amongst an array of strings.'''
strs = ["flower","flow","flight"]
for i in range(1,len(strs)):
    j=0
    while j < len(strs[0]) and j < len(strs[i]) and strs[0][j] == strs[i][j]:
        j += 1
    else:
        strs[0]=strs[0][:j]
print(strs[0])


#SAME AS ABOVE BUT EASY TO UNDERSTAND BUT A LITTLE BIGGER SPACE COMPLEXITY
# ans=strs[0]
# for i in range(1,len(strs)):
#     j=0
#     while j < len(ans) and j < len(strs[i]) and ans[j] == strs[i][j]:
#         j += 1
#     else:
#         ans=ans[:j]
# print(ans)

#WORST AS HIGH SPACE AND TIME COMPLEXITY WITH TWO FOR LOOPS
# ans=strs[0]
# for i in strs:
#     for j in range(min(len(ans),len(i))):
#         if ans[j]!=i[j]:
#             ans=ans[:j]
#             break
#     if len(i) < len(ans):
#         ans = ans[:len(i)]
# print(ans)