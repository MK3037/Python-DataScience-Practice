'''Return the smallest sorted list of ranges that cover all the numbers in the array exactly'''
nums = [0, 1, 2, 4, 5, 7]

def summaryRanges(nums):
    res = []
    start = nums[0]
    
    for i in range(len(nums)):
        # Check if we are at the last element OR if the next element is not consecutive
        if i + 1 == len(nums) or nums[i+1] != nums[i] + 1:
            
            if start == nums[i]:
                res.append(str(start))
            else:
                res.append(f"{start}->{nums[i]}")
            
            # If there's a next element, it becomes the new start
            if i + 1 < len(nums):
                start = nums[i+1]
                
    return res

print(summaryRanges(nums))
