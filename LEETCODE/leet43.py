x='20'
y='10'
#converting string to it int
def convert(a):
    n=0
    for i in range(len(a)):
        n=n*10
        n+=(ord(a[i]))-(ord('0'))
    return n

x=convert(x)
y=convert(y)

#multiplying the produced int
z=x*y
print(z)
print(chr(z))

#converting int back to string 
def convertback(a):
    n=''

    while a!=0:
        b=a%10
        a=a//10
        n+=chr(b+48)
    n=n[::-1]
    print(type(n))
    return n
print(convertback(z))