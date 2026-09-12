def pow(x,n):
    if n==0:
        return 1
    if n==1:
        return x
    if n==-1:
        return 1/x
    
    half=pow(x,n//2)
    if n%2==0:
        return half*half
    else:
        return x*half*half 

x=4
n=-2        #in python -3//2 is -2(floor funtion of -1.5 gives -2) NOTE while in c or java its -3/2 equals -1
print(pow(x,n))