def sumOfSquares(nums):
        sums=0
        n=len(nums)
        for i in range(1,n+1):
            if n%i==0:
                sums+=nums[i-1]**2
        return sums

n= [2,7,1,19,18,3]
print(sumOfSquares(n))



# def sumOfSquares(nums):
#         n = len(nums)
#         return sum(nums[i - 1] ** 2 for i in range(1, n + 1) if n % i == 0)