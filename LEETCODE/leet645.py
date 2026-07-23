class Solution(object):
    def findErrorNums(self, nums):
        count = {}
        n = len(nums)
        
        # Step 1: Count frequency of each number
        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        duplicate = missing = 0
        
        # Step 2: Check which number occurs twice and which is missing
        for i in range(1, n + 1):
            if i in count:
                if count[i] == 2:
                    duplicate = i
            else:
                missing = i
        
        return [duplicate, missing]

nums = [1, 2, 2, 4]
obj = Solution()
result = obj.findErrorNums(nums)
print("Duplicate and Missing:", result)
