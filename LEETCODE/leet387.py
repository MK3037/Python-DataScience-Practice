def firstUniqChar(self, s):
        ans = {}
        for i in s:
            ans[i] = ans.get(i, 0) + 1
        for idx, ch in enumerate(s):   
            if ans[ch] == 1:
                return idx
        return -1

s = "leetcode"
print(firstUniqChar(s))

# class Solution(object):                       MY CODE BUT O(N^2)
#     def firstUniqChar(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         ans={}
#         for i in s:
#             ans[i]=ans.get(i,0)+1
#         for i in ans:
#             if ans[i]==1:
#                 return s.index(i)             N^2 because it has to loop back here to find the index
#         else:
#             return -1
        