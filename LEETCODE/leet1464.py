def maxProduct(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        return (nums[n - 1] - 1) * (nums[n - 2] - 1)
nums=[3,4,5,2]
print(maxProduct(nums))