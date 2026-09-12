def firstStableIndex(nums, k):
        maxi=[]
        ma=nums[0]
        mi=nums[len(nums)-1]
        mini=[]
        for i in reversed(nums):
            if i<mi:
                mi=i
            mini.append(mi)
        for j in nums:
            if j>ma:
                ma=j
            maxi.append(ma)
        for index, (i,j) in enumerate(zip(maxi,mini[::-1]),start=0):
            if (i-j)<=k:
                  return index
        return -1

nums = [5,0,1,4]
k = 3
print(firstStableIndex(nums,k))