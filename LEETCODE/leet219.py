def containsNearbyDuplicate(nums, k):
        freq={}
        left=0
        k = min(k, len(nums) - 1)

        for i in range(k+1):
            freq[nums[i]]=freq.get(nums[i],0)+1
            if freq[nums[i]]==2:
                return True

        for right in range(k+1 ,len(nums)):
            freq[nums[left]]-=1
            left+=1

            freq[nums[right]]=freq.get(nums[right],0)+1
            if freq[nums[right]]>=2:
                return True
            
            
        
        return False
nums = [1,2,3,1]
k = 3
print(containsNearbyDuplicate(nums,k))