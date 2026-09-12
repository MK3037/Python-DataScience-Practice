def firstStableIndex(nums, k):
        score=0
        for i in range(len(nums)):
            maxi=max(nums[0:i+1])
            mini=min(nums[i:])

            score=maxi-mini
            if score<k:
                return i
        return -1
nums = [5,0,1,4]
k = 3
print(firstStableIndex(nums,k))