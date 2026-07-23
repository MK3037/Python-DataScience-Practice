'''6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.'''
class Solution(object):
    def pivotInteger(self, n):
        t_sum = (n*(n+1) // 2 )
        n = t_sum**0.5 

        if n == int(n) :
            return int(n) 
        return -1
x=Solution()
print(x.pivotInteger(8))
        
# class Solution(object):
#     def pivotInteger(self, n):
#         def sum(i):
#             return (i*(i+1)/2)
#         if n==1:
#             return 1
#         for i in range(1,n):
#             if sum(i)==(sum(n)+i-sum(i)):
#                 return i
#         return -1