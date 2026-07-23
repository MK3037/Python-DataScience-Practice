#mistake was doing max and not min
def minSubArrayLen(target, nums):
    left=0
    mi = float('inf')
    sums=0

    for right in range(len(nums)):
        sums+=nums[right]

        while sums>=target:
            mi=min(mi,right-left+1)
            sums-=nums[left]
            left+=1
                
    return mi if mi != float('inf') else 0

print(minSubArrayLen(7,[2,3,1,2,4,3]))