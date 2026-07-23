'''Given a non-negative integer x, return the square root of x rounded down to the nearest integer. '''

a=8
low=0       
high=a
ans=0
while low<=high:
    middle=(low+high)//2
    square=middle*middle

    if (square)==a:
        ans=middle
        break
    elif (square)<a:
        ans=middle
        low=middle+1
    else:
        high=middle-1
print(ans)
   

