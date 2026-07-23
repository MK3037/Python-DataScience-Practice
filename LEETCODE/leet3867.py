def gcdSum(nums):
        def GCDf(x, y):         # gcd found as in leet3658 isnt wont work due to high time complexity. this is Euclidean algorithm. 
            while y:
                x, y = y, x % y
            return x

        prefixGcd=[]
        mx=0
        for i in range(len(nums)):
            mx=max(mx,nums[i])
            mxigcd=GCDf(nums[i],mx)
            prefixGcd.append(mxigcd)

        prefixGcd.sort()

        sums=0
        left=0
        right=len(prefixGcd)-1
        while left<right:
            sums+=GCDf(prefixGcd[left],prefixGcd[right])
            left+=1
            right-=1
        return sums

print(gcdSum([3,6,2,8]))
