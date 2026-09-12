def isAnagram(s, t):
        if len(s) != len(t):
            return False

        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True

s = "anagram"
t = "nagaram"
print(isAnagram(s,t))




# class Solution(object):
#     def isAnagram(self, s, t):
#         if len(s) != len(t):
#             return False

#         counts = {}

#         for i in range(len(s)):
#             counts[s[i]] = 1 + counts.get(s[i],0)
#             counts[t[i]] = counts.get(t[i],0) - 1
        
#         for c in counts.values():
#             if c != 0:
#                 return False
#         return True
        


        

        




    
        
        