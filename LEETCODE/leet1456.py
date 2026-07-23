def maxVowels(s, k):
        vowels={'a','e','i','o','u'}
        currentcount=sum(1 for i in range(k) if s[i] in vowels)
        max_count=currentcount   

        for i in range(k,len(s)):
            currentcount+=(1 if s[i] in vowels else 0)
            currentcount-=(1 if s[i-k] in vowels else 0)

            if currentcount>max_count:
                max_count=currentcount
            if max_count==k:
                return k
        return max_count

print(maxVowels('abciiidef',3))