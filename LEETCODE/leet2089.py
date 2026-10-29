def targetIndices(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        freq=0
        count=0
        ans=[]
        for i in nums:
            if i==target:
                freq+=1
            elif i<target:
                count+=1
        return [i for i in range(count,count+freq)]

nums = [1,2,5,2,3]
target = 2
print(targetIndices(nums,target))



# class Solution(object):
#     def targetIndices(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         nums.sort()
#         ans=[]
#         for i,n in enumerate(nums):
#             if n==target:
#                 ans.append(i)
#             elif n>target:
#                 break
#         return ans