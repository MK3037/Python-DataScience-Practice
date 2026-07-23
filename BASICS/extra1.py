'''Count how many numbers from 1 to num have a "Digit Sum" that is an even number.'''
num=30
ans=[]
def sum_of_digit(n):
    sum=0
    while n!=0:
        sum=sum+n%10
        n=n//10
    return sum
for i in range(num):
    sum=sum_of_digit(i)
    if sum%2==0:
        ans.append(i)
print(ans)