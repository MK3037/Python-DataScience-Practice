'''Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.'''
class Solution(object):
    def findDisappearedNumbers(self, nums):
        ans = []
        for i in range(1, len(nums) + 1):
            if i not in nums:
                ans.append(i)
        return ans
sol=Solution()
my_list=[4,3,2,7,8,2,3,1]
print(sol.findDisappearedNumbers(my_list))