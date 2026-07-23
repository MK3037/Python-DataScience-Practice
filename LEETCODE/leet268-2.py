def missingNumber(nums):
    n = len(nums)
    # Start with n because the loop only goes up to n-1
    res = n 
    
    for i in range(n):
        # XOR the index and the value at that index
        res ^= i ^ nums[i]
        
    return res
