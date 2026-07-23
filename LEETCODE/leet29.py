dividend = 10
divisor = 3
a1 = abs(dividend)
b1 = abs(divisor)
ans_linear = 0

while a1 >= b1: 
    ans_linear += 1
    a1 -= b1
print(f"Linear Subtraction Result: {ans_linear}")

a2 = abs(dividend)
b2 = abs(divisor)
ans_bitshift = 0

while a2 >= b2:
    temp_divisor = b2
    multiplier = 1
    
    while a2 >= (temp_divisor << 1):
        temp_divisor <<= 1
        multiplier <<= 1
    
    a2 -= temp_divisor
    ans_bitshift += multiplier

print(f"Bit Shifting Result: {ans_bitshift}")



# Start
# │
# ├─ a2 = 43
# ├─ b2 = 5
# ├─ ans_bitshift = 0
# │
# ├─ while a2 >= b2   (43 >= 5) ✅
# │
# │   ├─ temp_divisor = 5
# │   ├─ multiplier  = 1
# │   │
# │   ├─ inner while a2 >= (temp_divisor << 1)
# │   │
# │   ├─ (5 << 1) = 10
# │   │   ├─ 43 >= 10 ✅
# │   │   │   ├─ temp_divisor = 10
# │   │   │   └─ multiplier  = 2
# │   │
# │   ├─ (10 << 1) = 20
# │   │   ├─ 43 >= 20 ✅
# │   │   │   ├─ temp_divisor = 20
# │   │   │   └─ multiplier  = 4
# │   │
# │   ├─ (20 << 1) = 40
# │   │   ├─ 43 >= 40 ✅
# │   │   │   ├─ temp_divisor = 40
# │   │   │   └─ multiplier  = 8
# │   │
# │   ├─ (40 << 1) = 80
# │   │   └─ 43 >= 80 ❌ → stop inner loop
# │   │
# │   ├─ a2 = a2 - temp_divisor
# │   │   └─ a2 = 43 - 40 = 3
# │   │
# │   ├─ ans_bitshift = ans_bitshift + multiplier
# │   │   └─ ans_bitshift = 0 + 8 = 8
# │
# ├─ while a2 >= b2   (3 >= 5) ❌
# │
# └─ Exit loop
