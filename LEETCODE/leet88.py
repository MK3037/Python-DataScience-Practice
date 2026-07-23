num1 = [1, 2, 3]
num2 = [2, 5, 6]
m = len(num1) 
n = len(num2)

for i in range(len(num2)):
    num1.append(0)
    
last = m + n - 1
m -= 1
n -= 1

while m >= 0 and n >= 0:
    if num1[m] > num2[n]:
        num1[last] = num1[m]
        m -= 1
    else:
        num1[last] = num2[n]
        n -= 1
    last -= 1

while n >= 0:
    num1[last] = num2[n]
    n -= 1
    last -= 1

print(num1)