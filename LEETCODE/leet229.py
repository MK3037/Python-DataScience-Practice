def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count={}
        ans=[]
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for key, values in count.items():
            if values > len(nums)//3:
                ans.append(key)
        return ans 
print(majorityElement([3,2,3]))