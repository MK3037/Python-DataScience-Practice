'''Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.'''
num = 38
def sum_of_digit(x):
    sum=0
    while x>0:
        sum=sum+(x%10)
        x=x//10
    return sum

while num>9:
    num=sum_of_digit(num)
print(num)