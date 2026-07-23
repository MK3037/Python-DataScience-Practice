def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
def fibonacci_fast(n):
    if n <= 1:
        return n
    return fibonacci_fast(n-1) + fibonacci_fast(n-2)
def sum(n,s=0):
    if n==0:
        return s
    else:
        x=n%10
        return sum(n//10,s+x)


print(sum(1234))
print(fibonacci_fast(6))
print(factorial(4))
