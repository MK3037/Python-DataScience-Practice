strs = ["eat","tea","tan","ate","nat","bat"]
freq={s:{j:s.count(j) for j in set(s)} for s in strs}
visited=set()
ans=[]
i=0
while i in range(len(strs)):
    if strs[i] in visited:
        i+=1
        continue
    temp=[strs[i]]
    visited.add(strs[i])
    for j in range(i+1,len(freq)):
        if freq[strs[i]]==freq[strs[j]]:
            temp.append(strs[j])
            visited.add(strs[j])
    ans.append(temp)
    i+=1

print(ans)

# class Solution(object):
#     def groupAnagrams(self, strs):
#        a={}
#        for i in strs:
#             b=''.join(sorted(i))
#             if b not in a:
#                 a[b]=[]
#             a[b].append(i)
#        return list(a.values())


        