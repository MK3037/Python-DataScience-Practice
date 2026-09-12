def maximumLengthSubstring(s):
        freq={}
        slow=0
        maxlength=0
        i=0
        while i<len(s):             #search claude the code if it was a for loop here
            freq[s[i]]=freq.get(s[i],0)+1
            while freq[s[i]]>2:
                freq[s[slow]]-=1
                slow+=1
            i+=1
            maxlength=max(maxlength,i-slow)
            print(s[slow:i])
        print(freq)
        return maxlength

s = "bcbbbcba"
print(maximumLengthSubstring(s))