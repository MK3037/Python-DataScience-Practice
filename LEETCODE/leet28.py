'''Given two strings needle and haystack, 
return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack'''
haystack = "sadbutsad"
needle = "but"
found = False

for i in range(len(haystack) - len(needle) + 1):
    j = 0
    while j < len(needle) and haystack[i + j] == needle[j]:
        j += 1
    if j == len(needle):
        print(i)   # index where needle starts
        found = True
        break
    

if not found:
    print(-1)