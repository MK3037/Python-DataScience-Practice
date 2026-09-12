def lengthOfLongestSubstring(s):   #without duplicates
        left =0
        seen={}
        ma=0

        for right in range(len(s)):
            seen[s[right]]=seen.get(s[right],0)+1

            while seen.get(s[right],0)>1 :
                seen[s[left]]-=1
                left+=1
            
            ma=max(ma,right-left+1)

        return ma

print(lengthOfLongestSubstring('abcabcbb'))