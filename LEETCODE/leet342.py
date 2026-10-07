def isPowerOfFour(n):
        if n<=0:
            return False
        else:
            while n%4==0:
                n=n/4
        return n==1

n = 16
print(isPowerOfFour(n))