'''Given two binary strings a and b, return their sum as a binary string.'''

a = "1010"
b = "1011"

carry = 0
result = ""

list_a = list(a)
list_b = list(b)

while list_a or list_b or carry:
    if list_a:
        carry += int(list_a.pop())
    
    if list_b:
        carry += int(list_b.pop())
    
    result = str(carry % 2) + result
    carry //= 2

print(result)