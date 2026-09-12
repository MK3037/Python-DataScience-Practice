def maxSubarrayLength(nums, k):
        freq={}
        slow=0
        fast=0
        maxlength=0
        while fast<len(nums):
            freq[nums[fast]]=freq.get(nums[fast],0)+1
            while freq[nums[fast]]>k:
                  freq[nums[slow]]=freq[nums[slow]]-1
                  slow+=1
            fast+=1
            maxlength=max(maxlength,fast-slow)
        print(maxlength)
        return freq


nums =[1,4,4,3]
k = 1

print(maxSubarrayLength(nums,k))