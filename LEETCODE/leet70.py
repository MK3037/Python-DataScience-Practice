'''You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?'''
n=5
one,two=1,1
for i in range(n-1):
    temp=one
    one=one+two
    two=temp
print(one)

# Start
# │
# ├─ n = 5
# ├─ one = 1   (ways to reach step 1)
# ├─ two = 1   (ways to reach step 0)
# │
# ├─ for i in range(n - 1)   → range(4)
# │
# ├─ i = 0
# │   │
# │   ├─ temp = one
# │   │   temp = 1
# │   │
# │   ├─ one = one + two
# │   │   one = 1 + 1 = 2
# │   │
# │   └─ two = temp
# │       two = 1
# │
# ├─ i = 1
# │   │
# │   ├─ temp = one
# │   │   temp = 2
# │   │
# │   ├─ one = one + two
# │   │   one = 2 + 1 = 3
# │   │
# │   └─ two = temp
# │       two = 2
# │
# ├─ i = 2
# │   │
# │   ├─ temp = one
# │   │   temp = 3
# │   │
# │   ├─ one = one + two
# │   │   one = 3 + 2 = 5
# │   │
# │   └─ two = temp
# │       two = 3
# │
# ├─ i = 3
# │   │
# │   ├─ temp = one
# │   │   temp = 5
# │   │
# │   ├─ one = one + two
# │   │   one = 5 + 3 = 8
# │   │
# │   └─ two = temp
# │       two = 5
# │
# └─ loop ends
