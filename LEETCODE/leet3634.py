'''Given an array of integers nums and an integer k, 
remove the minimum number of elements such that in the remaining array, 
the maximum element is at most k times the minimum element.'''
def min_removals(nums, k):
    nums.sort()
    left = 0
    max_kept = 0

    for right in range(len(nums)):
        while nums[right] > k * nums[left]:
            left += 1
        max_kept = max(max_kept, right - left + 1)

    return len(nums) - max_kept


# Simple test cases
nums1 = [1, 3, 6, 2, 5]
k1 = 2
print(min_removals(nums1, k1))   # Output: 2

nums2 = [1, 2, 3, 4, 5]
k2 = 3
print(min_removals(nums2, k2))   # Output: 1
