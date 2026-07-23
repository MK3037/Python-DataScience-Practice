def maximumSubarraySum(nums, k):
        sums=0
        maxsums=0
        freq={}

        for i in range(k):
            freq[nums[i]]=freq.get(nums[i],0)+1
            sums+=nums[i]
        if len(freq) == k:
            maxsums = sums

        for i in range(k,len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1
            freq[nums[i-k]]-=1
            
            if freq[nums[i-k]] == 0:
                del freq[nums[i-k]]
            sums=sums+nums[i]-nums[i-k]
            if len(freq) == k:
                maxsums = max(maxsums, sums)
        return maxsums

nums = [1,5,4,2,9,9,9]
k = 3
print(maximumSubarraySum(nums,k))