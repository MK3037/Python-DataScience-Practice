nums = [2,0, 1, 0, 0,3, 12,13]

def moveZeros(nums):
    i=0
    for j in range(len(nums)):
        if nums[j]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
    return nums

print(moveZeros(nums))




# i=0
# j=0
# [2, 0, 1, 0, 0, 3, 12, 13]
# will compare

# i=1
# j=1
# [2, 0, 1, 0, 0, 3, 12, 13]

# i=1
# j=2
# [2, 0, 1, 0, 0, 3, 12, 13]
# will compare

# i=2
# j=3
# [2, 1, 0, 0, 0, 3, 12, 13]

# i=2
# j=4
# [2, 1, 0, 0, 0, 3, 12, 13]

# i=2
# j=5
# [2, 1, 0, 0, 0, 3, 12, 13]
# will compare

# i=3
# j=6
# [2, 1, 3, 0, 0, 0, 12, 13]
# will compare

# i=4
# j=7
# [2, 1, 3, 12, 0, 0, 0, 13]
# will compare

# i=5
# j ends
# [2, 1, 3, 12, 13, 0, 0, 0]



