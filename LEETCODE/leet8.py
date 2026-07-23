'''STRING TO INTEGER'''
a = "-32A2"
negative = False
x = 0

for i in a:
    if i == "-":
        negative = True
    elif i == "+":
        continue
    elif '0' <= i <= '9':
        x = x * 10 + (ord(i) - 48)
    else:
        break
if negative:
    x = -x

# LeetCode 8 requires clamping to 32-bit integer range
x = max(-2**31, min(x, 2**31 - 1))

print(x)




# Start
# │
# ├─ a = "-32A2"
# ├─ negative = False
# ├─ x = 0
# │
# ├─ for i in a
# │
# ├─ i = '-'
# │   │
# │   ├─ i == '-' ? ✅
# │   │
# │   └─ negative = True
# │
# ├─ i = '3'
# │   │
# │   ├─ i == '-' ? ❌
# │   ├─ i == '+' ? ❌
# │   ├─ '0' <= i <= '9' ? ✅
# │   │
# │   └─ x = x * 10 + (ord('3') - 48)
# │       x = 0 * 10 + 3 = 3
# │
# ├─ i = '2'
# │   │
# │   ├─ i == '-' ? ❌
# │   ├─ i == '+' ? ❌
# │   ├─ '0' <= i <= '9' ? ✅
# │   │
# │   └─ x = x * 10 + (ord('2') - 48)
# │       x = 3 * 10 + 2 = 32
# │
# ├─ i = 'A'
# │   │
# │   ├─ i == '-' ? ❌
# │   ├─ i == '+' ? ❌
# │   ├─ '0' <= i <= '9' ? ❌
# │   │
# │   └─ else → break
# │
# └─ loop ends
