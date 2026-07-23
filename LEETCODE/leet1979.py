def findGCD(nums):

        x=min(nums)
        y=max(nums)
        ans=1
        for i in range(2,x+1):
            while x%i==0 and y%i==0:
                x=x/i
                y=y/i
                ans*=i

        return ans

print(findGCD([2,5,6,9,10]))