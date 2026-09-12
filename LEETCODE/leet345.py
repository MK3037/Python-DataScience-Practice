def reverseVowels(s):
        x=list("aeiouAEIOU")
        left=0
        right=len(s)-1
        s=list(s)
        while left<right:
            if s[left] not in x:
                left+=1
            elif s[right] not in x:
                right-=1
            elif s[left] and s[right] in x:
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
        return "".join(s)

s = "IceCreAm"
print(reverseVowels(s))