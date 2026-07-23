'''Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i]'''
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        # 1. Sort the numbers to determine their rank
        sor = sorted(nums)
        out = []
        
        # 2. For every number in the original list
        for i in range(len(nums)):
            # .index() finds the FIRST time the number appears in the sorted list.
            # That index is exactly how many numbers are smaller than it.
            count = sor.index(nums[i])
            out.append(count)
            
        return out

sol = Solution()
my_list = [8, 1, 2, 2, 3]
result = sol.smallerNumbersThanCurrent(my_list)
print(result)