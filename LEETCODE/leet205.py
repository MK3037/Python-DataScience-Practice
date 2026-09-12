def isIsomorphic(s, t):
        if len(s)!=len(t):
            return False
        dist={}
        distt={}
        for i in range(len(s)):
            if dist.get(s[i],t[i])!=t[i]:
                return False
            if distt.get(t[i],s[i])!=s[i]:
                return False
            dist[s[i]]=t[i]
            distt[t[i]]=s[i]
        return True

s = "egg"
t = "add"
print(isIsomorphic(s,t))

s="bbbaaaba"
t="aaabbbba"
print(isIsomorphic(s,t))



# def isIsomorphic(self, s, t):
#         return len(set(zip(s, t))) == len(set(s)) == len(set(t))