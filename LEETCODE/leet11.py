x=[1,8,6,2,5,4,8,3,7]
area=0
max_area=0
for i in range (len(x)):
    for j in range(i,len(x)):
        if(x[i]>x[j]):
            h=x[j]          #height
        else:
            h=x[i]
        b=(j-i)             #breadth
        area=h*b
        if area>max_area:
            max_area=area
print("reaquired area is",max_area)




# Start
# │
# ├─ x = [1,8,6,2,5,4,8,3,7]
# ├─ area = 0
# ├─ max_area = 0
# │
# ├─ for i in range(len(x))   → range(9)
# │
# ├─ i = 0   (x[i] = 1)
# │   │
# │   ├─ for j in range(i, len(x))
# │   │
# │   ├─ j = 0
# │   │   │
# │   │   ├─ h = min(x[0], x[0]) = 1
# │   │   ├─ b = j - i = 0
# │   │   ├─ area = 1 * 0 = 0
# │   │   └─ max_area remains 0
# │   │
# │   ├─ j = 1
# │   │   │
# │   │   ├─ h = min(1, 8) = 1
# │   │   ├─ b = 1
# │   │   ├─ area = 1 * 1 = 1
# │   │   └─ max_area = 1
# │   │
# │   ├─ j = 2
# │   │   │
# │   │   ├─ h = min(1, 6) = 1
# │   │   ├─ b = 2
# │   │   ├─ area = 2
# │   │   └─ max_area = 2
# │   │
# │   ├─ j = 3 → area = 3 → max_area = 3
# │   ├─ j = 4 → area = 4 → max_area = 4
# │   ├─ j = 5 → area = 5 → max_area = 5
# │   ├─ j = 6 → area = 6 → max_area = 6
# │   ├─ j = 7 → area = 7 → max_area = 7
# │   ├─ j = 8 → area = 8 → max_area = 8
# │
# ├─ i = 1   (x[i] = 8)
# │   │
# │   ├─ j = 1 → h=8, b=0 → area=0 → no change
# │   │
# │   ├─ j = 2
# │   │   │
# │   │   ├─ h = min(8,6) = 6
# │   │   ├─ b = 1
# │   │   ├─ area = 6
# │   │   └─ max_area remains 8
# │   │
# │   ├─ j = 3 → h=2, b=2 → area=4
# │   ├─ j = 4 → h=5, b=3 → area=15 → max_area = 15
# │   ├─ j = 5 → h=4, b=4 → area=16 → max_area = 16
# │   ├─ j = 6 → h=8, b=5 → area=40 → max_area = 40
# │   ├─ j = 7 → h=3, b=6 → area=18
# │   ├─ j = 8 → h=7, b=7 → area=49 → max_area = 49
# │
# ├─ i = 2   (x[i] = 6)
# │   │
# │   ├─ j = 2 → area=0
# │   ├─ j = 3 → h=2, b=1 → area=2
# │   ├─ j = 4 → h=5, b=2 → area=10
# │   ├─ j = 5 → h=4, b=3 → area=12
# │   ├─ j = 6 → h=6, b=4 → area=24
# │   ├─ j = 7 → h=3, b=5 → area=15
# │   ├─ j = 8 → h=6, b=6 → area=36
# │
# ├─ i = 3 → (areas computed, none > 49)
# ├─ i = 4 → (areas computed, none > 49)
# ├─ i = 5 → (areas computed, none > 49)
# ├─ i = 6 → (areas computed, none > 49)
# ├─ i = 7 → (areas computed, none > 49)
# ├─ i = 8 → j=8 → area=0
# │
# └─ loops end
