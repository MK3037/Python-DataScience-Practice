def reverseDegree(s):
        sum=0
        for i in range(len(s)):
            sum=sum+(i+1)*(26-(ord(s[i])-97))
        return sum

s = "abc"
print(reverseDegree(s))
    