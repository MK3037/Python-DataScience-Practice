'''Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x'''
def square(n):
    if n<=0:    return False
    if n==1:    return True
    if n%2!=0:  return False
    return square(n//2)
print(square(15))



# def square(n):
#     if n<1:                   #n=4   100   then 3 is 011       and 100 & 011 is 0 
#         return False          #n=8   1000  then 7 is 0111 
#     if n & (n-1)==0:                            
#         return True
#     return False

