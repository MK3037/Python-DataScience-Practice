n=104
num=0
su=0
while n>0:
    if n%10!=0:
        num=(num*10)+(n%10)
        su+=n%10
    n=n//10
    print(n)

num=int(str(num)[::-1])             #num = int(str(n).replace("0", "")) easy way
print(num*su)
   