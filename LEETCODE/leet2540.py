nums1 = [1,2,3,6]
nums2 = [2,3,4,5]



nums1=set(nums1)            # Convert, intersect, and convert back to a list
nums2=set(nums2)            #nums3 = list(set(nums1) & set(nums2)) if wants to do directly on list nums1

nums3= nums1 & nums2

if nums3:
    print(min(nums3))       #min throws error if nums3=[]


# class Solution(object):
#     def getCommon(self, nums1, nums2):
#         i = j = 0
#         while i < len(nums1) and j < len(nums2):
#             if nums1[i] == nums2[j]:
#                 return nums1[i]
#             elif nums1[i] < nums2[j]:
#                 i += 1
#             else:
#                 j += 1
#         return -1   