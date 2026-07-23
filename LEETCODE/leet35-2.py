'''have to use binary search as mentioned that time complexity is O(log n)
in earlier linear search, its much higher, O(n)'''
def searchInsert(nums, target):
    low = 0
    high = len(nums) - 1 

    while low <= high:
        mid = (low + high) // 2  # Find the middle index. floor division
       
        if nums[mid] == target:
            return mid # Found it!,   break
        elif nums[mid] < target:
            low = mid + 1 # Look in the right half
        else:
            high = mid - 1 # Look in the left half
  
    # If not found, 'low' will be the correct insertion index
    return low


num = [1,2,5,6,8,9]
target = 7
print("it should be at", searchInsert(num, target) + 1, "position")
