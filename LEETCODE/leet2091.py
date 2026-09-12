def minimumDeletions(nums):
        minn=maxx=nums[0]
        posmin=posmax=0
        for i in range(len(nums)):
            if nums[i]>maxx:
                maxx=nums[i]
                posmax=i
            elif nums[i]<minn:
                minn=nums[i]
                posmin=i
        
        sc1=0+max(posmax,posmin)+1  #removing both from front
        sc2=len(nums)-min(posmax,posmin)    #removing both from back
        sc3=(0+min(posmax,posmin)+1)+(len(nums)-max(posmax,posmin)) #removing one from front and other from back
        return min(sc1,sc2,sc3)

nums=[2,10,7,5,4,1,8,6]
print(minimumDeletions(nums))