def longestPalindrome(s):
        ans=""
        for i in range(1,len(s)):
            #odd length
            x=1
            while i-x>=0 and i+x<len(s) and s[i-x]==s[i+x]:
                x+=1
            else:
                temp=s[i-x+1:i+x]
        
            if len(temp)>len(ans):
                ans=temp

            #even length
            x = 0
            while i-1-x >= 0 and i+x < len(s) and s[i-1-x] == s[i+x]:
                x += 1
            else:
                temp = s[i-x:i+x]

            if len(temp) > len(ans):
                ans = temp
        return ans

s = "babad"
print(longestPalindrome(s))