def maximumProduct(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if nums[0]*nums[1]*nums[-1]>nums[-3]*nums[-2]*nums[-1]:
            return nums[0]*nums[1]*nums[-1]
        return nums[-3]*nums[-2]*nums[-1]

nums = [1,2,3]
print(maximumProduct(nums))