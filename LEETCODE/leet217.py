def containsDuplicate(nums):
        sets=set()
        for i in nums:
            if i in sets:
                return True
            sets.add(i)
        return False
nums = [1,2,3,1]
print(containsDuplicate(nums))