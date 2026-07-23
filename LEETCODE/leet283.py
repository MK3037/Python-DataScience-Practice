'''Given an integer array nums, 
move all 0's to the end of it while maintaining the relative order of the non-zero elements.'''
def moveZeroes(nums):
    last_non_zero = 0
    
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero] = nums[i]
            last_non_zero += 1
    for i in range(last_non_zero, len(nums)):       #filling remianing with 0
        nums[i] = 0

nums = [0, 1, 0, 0, 3, 12]
moveZeroes(nums)
print(nums)