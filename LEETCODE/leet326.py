def isPowerOfThree(n):
        if n==1:
            return True
        def pow(x):
            if x>n:
                return False
            elif x==n:
                return True
            else:
                return pow(3*x)
        return pow(3)

n = 27
print(isPowerOfThree(n))