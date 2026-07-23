'''A sequence of numbers is called an arithmetic progression 
if the difference between any two consecutive elements is the same'''
class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        differences = {arr[i] - arr[i-1] for i in range(1, len(arr))}
        return len(differences) == 1

arr = [3,5,1]
x=Solution()
print(x.canMakeArithmeticProgression(arr))

# class Solution(object):
#     def canMakeArithmeticProgression(self, arr):
#         arr.sort()
#         y=arr[1]-arr[0]
#         for i in range(1,len(arr)):
#             z=arr[i]-arr[i-1]
#             if y!=z:
#                 return False
#         return True
            