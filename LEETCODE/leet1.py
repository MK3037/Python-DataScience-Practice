#TWO SUMS THAT REACH TARGET, only one unizue pair exists, else would have to modify this logic
class Solution(object):
    def twoSum(self, nums, target):
        result = []
        
        for i in range(len(nums)):
            # create a list excluding the current element
            temp = nums[:i] + nums[i+1:]
            # check if the required number exists
            if (target - nums[i]) in temp:
                result.append(i)
                if len(result) == 2:
                    break   # STOP after two indices
        return result


nums = [2, 7, 11, 15]
target = 9

obj = Solution()
ans = obj.twoSum(nums, target)

print("Array:", nums)
print("Target:", target)
print("Indices:", ans)
