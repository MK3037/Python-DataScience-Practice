'''Given a binary array nums, return the maximum number of consecutive 1's in the array.'''
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_count, count = 0, 0
        for i in nums:
            if i == 1:
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 0
        return max_count

# ---- Driver code ----
nums = [1, 1, 0, 1, 1, 1]  # Example input
obj = Solution()
result = obj.findMaxConsecutiveOnes(nums)

print("Input Array:", nums)
print("Maximum Consecutive Ones:", result)
