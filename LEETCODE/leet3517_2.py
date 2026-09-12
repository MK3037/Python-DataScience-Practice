def smallestPalindrome(s, k):
    freq={}
    n=len(s)//2
    mid=""
    for i in range(97,123):
        freq[chr(i)]=0
    print(freq)
    for i in range(n):
        freq[s[i]]=freq.get(s[i],0)+1
    print(freq)
    ans=[]

    for i in freq:
        if freq[i]>0:
            ans.append(i*freq[i])
    ans="".join(ans)
    print(ans)

    if n%2==0:
        mid=s[n//2]
    return ans+mid+ans[::-1]
s = "aabbaa"
k = 2
print(smallestPalindrome(s,k))
