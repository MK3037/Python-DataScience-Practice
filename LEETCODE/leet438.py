import string
def findAnagrams(s, p):
        if len(s) < len(p):
            return []

        const={letter: 0 for letter in string.ascii_lowercase}
        dynam=const.copy()
        index=[]
        for i in p:
            const[i]+=1

        k = len(p)
        for i in range(k):
            dynam[s[i]] += 1
        if const == dynam:
            index.append(0)

        for i in range(k,len(s)):
            dynam[s[i]]+=1
            dynam[s[i-k]]-=1

            if const==dynam:
                index.append(i-k+1)

        return index

print(findAnagrams('cbaebabacd','abc'))