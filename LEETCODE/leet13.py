'''FROM ROMAN'''
roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
integer = [1, 5, 10, 50, 100, 500, 1000]

inp = input("enter the roman number u want: ")  #iv
ans = 0

for i in range(len(inp)):
    # Get the value of the current symbol
    curr_val = integer[roman.index(inp[i])]             #current symbol curr_val
    
    # Check if there is a next symbol (its not the end)
    if i + 1 < len(inp):
        next_val = integer[roman.index(inp[i+1])]       #next symbol stored in next_val
        
        if curr_val < next_val:
            ans -= curr_val
        else:
            ans += curr_val
    # Last character always gets added
    else:
        ans += curr_val

print(ans)



# Start
# │_IV
# ├─ ans = 0
# │
# ├─ for i in range(len(inp))   → range(2)
# │
# ├─ i = 0
# │   │
# │   ├─ inp[i]   = 'I'
# │   ├─ curr_val = 1
# │   │
# │   ├─ i + 1 < len(inp) ?  (1 < 2) ✅
# │   │   │
# │   │   ├─ inp[i+1] = 'V'
# │   │   ├─ next_val = 5
# │   │   │
# │   │   ├─ curr_val < next_val ?  (1 < 5) ✅
# │   │   │
# │   │   └─ ans = ans - curr_val
# │   │       ans = 0 - 1 = -1
# │
# ├─ i = 1   (last index)
# │   │
# │   ├─ inp[i]   = 'V'
# │   ├─ curr_val = 5
# │   │
# │   ├─ i + 1 < len(inp) ?  (2 < 2) ❌
# │   │
# │   └─ else (last character)
# │       └─ ans = ans + curr_val
# │           ans = -1 + 5 = 4
# │
# └─ loop ends
#     │
#     └─ print(ans) → 4
