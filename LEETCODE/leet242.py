'''Given two strings s and t, return true if t is an anagram of s, and false otherwise'''
def isAnagram(s, t):
    if len(s) != len(t):
        return False
        
    counts_s = {}
    counts_t = {}
    
    for char in s:
        counts_s[char] = counts_s.get(char, 0) + 1
    for char in t:
        counts_t[char] = counts_t.get(char, 0) + 1
        
    return counts_s == counts_t  
s = "anagram"
t = "nagaram"
print(isAnagram(s,t))