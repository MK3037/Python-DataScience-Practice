'''A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not'''
def isHappy(n):
        def getsum(n):
            sums=0
            while n>0:
                x=n%10
                sums+=x*x
                n=n//10
            return sums
        
        seen = set()  
        while n != 1 and n not in seen:
            seen.add(n)
            n = getsum(n)
            
        return n == 1

number=19
if isHappy(number):
    print(f"{number} is a Happy Number!")
else:
    print(f"{number} is not a Happy Number.")





# def isHappy(n):       USING RECURENCE BUT TIME LIMIT EXCEED OR MAXIMUM RECURENCE DEPTH REACH ERROR
#         def sums(n,x):
#             if n==0:
#                 return False
#             elif x==1:
#                 return True
#             s=0
#             while x>0:
#                 s+=(x%10)**2
#                 x=x//10
#             return sums(n-1,s)
#         return sums(n,n)

# print(isHappy(19))