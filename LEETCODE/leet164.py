def maximumGap(nums):
        nums.sort()
        diff=0
        for i in range(1,len(nums)):
            currdiff=nums[i]-nums[i-1]
            diff=max(diff,currdiff)
        return diff

nums = [3,6,9,1]
print(maximumGap(nums))