def nextBeautifulNumber(n):
        def split(x):
            dic={}
            while x>0:
                y=x%10
                x=x//10
                dic[y]=dic.get(y,0)+1
            return all(key==value for key, value in dic.items())


        while True:
            n+=1
            if split(n):
                break
        return n
x=nextBeautifulNumber(2)
print(x)