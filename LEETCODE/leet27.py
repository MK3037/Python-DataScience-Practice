def removeElement(nums, val):
        left=0
        right=0
        while right<len(nums):
            if nums[right]!=val:
                nums[left]=nums[right]
                left+=1
            right+=1
        return left
nums = [3,2,2,3], val = 3
print(removeElement(nums,val))