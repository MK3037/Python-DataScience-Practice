'''Given an integer array nums of length n and an integer target, 
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.'''
nums = [-1, 2, 1, -4]
target = 1
nums.sort()     #[-4,-1,1,2]
closest_sum = float('inf')

for i in range(len(nums)):        
    low = i + 1                                 #imideate next element
    high = len(nums) - 1                                #to last element
    
    while low < high:                           #here i is fix and we play with low and high to find our need
        current_sum = nums[i] + nums[low] + nums[high]
        
        if abs(current_sum - target) < abs(closest_sum - target):
            closest_sum = current_sum
        
        if current_sum == target:               #found, exit
            closest_sum = current_sum
            break
        elif current_sum < target:              #search left
            low += 1
        else:                                   #search right
            high -= 1
            
    if closest_sum == target:
        break

print(closest_sum)

# Start
# │
# ├─ nums = [-4, -1, 1, 2]
# ├─ target = 1
# ├─ closest_sum = ∞
# │
# ├─ for i in range(n)
# │
# ├─ i = 0   (nums[i] = -4)
# │   │
# │   ├─ i > 0 and nums[i] == nums[i-1]? ❌
# │   │
# │   ├─ low = 1  (nums[low] = -1)
# │   ├─ high = 3 (nums[high] = 2)
# │   │
# │   ├─ while low < high ?  (1 < 3) ✅
# │   │   │
# │   │   ├─ current_sum = -4 + (-1) + 2 = -3
# │   │   │
# │   │   ├─ |current_sum - target|
# │   │   │   = |-3 - 1| = 4
# │   │   │
# │   │   ├─ |closest_sum - target|
# │   │   │   = |∞ - 1| = ∞
# │   │   │
# │   │   ├─ 4 < ∞ ? ✅
# │   │   │
# │   │   └─ closest_sum = -3
# │   │
# │   │   ├─ current_sum == target ? ❌
# │   │   ├─ current_sum < target ? (-3 < 1) ✅
# │   │   │
# │   │   └─ low = low + 1 → low = 2
# │   │
# │   ├─ while low < high ?  (2 < 3) ✅
# │   │   │
# │   │   ├─ current_sum = -4 + 1 + 2 = -1
# │   │   │
# │   │   ├─ |current_sum - target|
# │   │   │   = |-1 - 1| = 2
# │   │   │
# │   │   ├─ |closest_sum - target|
# │   │   │   = |-3 - 1| = 4
# │   │   │
# │   │   ├─ 2 < 4 ? ✅
# │   │   │
# │   │   └─ closest_sum = -1
# │   │
# │   │   ├─ current_sum == target ? ❌
# │   │   ├─ current_sum < target ? (-1 < 1) ✅
# │   │   │
# │   │   └─ low = 3
# │   │
# │   └─ while low < high ? (3 < 3) ❌
# │
# ├─ i = 1   (nums[i] = -1)
# │   │
# │   ├─ duplicate check ? ❌
# │   │
# │   ├─ low = 2 (nums[low] = 1)
# │   ├─ high = 3 (nums[high] = 2)
# │   │
# │   ├─ while low < high ? (2 < 3) ✅
# │   │   │
# │   │   ├─ current_sum = -1 + 1 + 2 = 2
# │   │   │
# │   │   ├─ |2 - 1| = 1
# │   │   ├─ |-1 - 1| = 2
# │   │   │
# │   │   ├─ 1 < 2 ? ✅
# │   │   │
# │   │   └─ closest_sum = 2
# │   │
# │   │   ├─ current_sum == target ? ❌
# │   │   ├─ current_sum < target ? ❌
# │   │   │
# │   │   └─ high = high - 1 → high = 2
# │   │
# │   └─ while low < high ? (2 < 2) ❌
# │
# ├─ i = 2
# │   │
# │   ├─ low = 3, high = 3
# │   └─ while low < high ? ❌
# │
# ├─ i = 3
# │   ├─ low = 4 (out of range)
# │   └─ while low < high ? ❌
# │
# └─ loop ends
