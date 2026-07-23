'''Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0'''
n = -32
x = 0

# 1. Store the sign and make n positive
sign = -1 if n < 0 else 1
n = abs(n)

# 2. Standard reversal logic (using // for integers)
while n > 0:
    x = x * 10
    x = x + (n % 10)
    n = n // 10

# 3. Restore the sign
x = x * sign

print(x)