x=int(input("enter a number:"))
num=0
y=x
while x>0:
    num=num*10
    num=num+(x%10)
    x=x//10
if num==y:
    print("true")
else:
    print("false")

    # def isPalindrome(self, x):
    #     return str(x)[::-1]==str(x)
