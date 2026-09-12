def longestConsecutive(nums):
        nums=set(nums)
        ans=0
        for i in nums:
            if i-1 not in nums:
                count=1
                while (i + count) in nums:
                    count += 1
                ans=max(ans,count)
        return ans
nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))