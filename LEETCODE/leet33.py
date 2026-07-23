def search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # 1. Identify which side is sorted
        # Check if the Left side is sorted
        if nums[left] <= nums[mid]:
            # Target is within the sorted left half
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        # 2. Otherwise, the Right side must be sorted
        else:
            # Target is within the sorted right half
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:  
                right = mid - 1
                
    return -1
nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums,target))