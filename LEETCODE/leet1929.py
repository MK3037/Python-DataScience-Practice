class Solution(object):
    def getConcatenation(self, nums):
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums

nums = [1, 2, 3]  
obj = Solution()
result = obj.getConcatenation(nums)

print("Input:", nums[:len(nums)//2]) 
print("Concatenated Array:", result)
