def smallestNumber(n, t):
        def product(prod,x):
            if x>0:
                return product(prod*(x%10),x//10)
            else:
                return prod
        for i in range(n,n**2+t):        #1^2 is 1 so for loop wont go and give null, thats why add 1. and its commmon to go till n**2 for solving this type of questions
            if product(1,i)%t==0:
                return i

print(smallestNumber(1,2))



# class Solution(object):
#     def smallestNumber(self, n, t):
#         """
#         :type n: int
#         :type t: int
#         :rtype: int
#         """
#         while True:
#             p=n
#             pr=1
#             while p>0:
#                 pr*=p%10
#                 p//=10
#             if pr%t==0:return n
#             n+=1
        