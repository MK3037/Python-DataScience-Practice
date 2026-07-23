
def separateDigits(nums):
    ans = []
    for i in nums:
        subans = []
        while i > 0:
            subans.append(i % 10)
            i //= 10
        ans.extend(subans[::-1])
    return ans

x=[21,324,45]

y=separateDigits(x)
print(y)



# class Solution:
#     def separateDigits(self, nums):
#         result=[]
#         for num in nums:
#             for digit in str(num):
#                 result.append(int(digit))
#         return result
        