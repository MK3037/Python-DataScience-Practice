def largestInteger(nums, k):
        slow=0
        count={}
        while slow+k-1<len(nums):
            sets=set()
            for i in range(slow,slow+k):
                if nums[i] not in sets:
                    count[nums[i]]=count.get(nums[i],0)+1
                    sets.add(nums[i])
            slow+=1
        ans=[keys for keys,value in count.items() if value==1]
        if ans:
            return max(ans)
        return -1

nums = [3,9,2,1,7]
k = 3
print(largestInteger(nums,k))
print(largestInteger([0,0],2))          #imp case