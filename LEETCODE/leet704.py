def search(nums, target):
        left=0
        right=len(nums)-1
        while left<=right:
            med=left+(right-left)//2
            if nums[med]==target:
                return med
            elif target<nums[med]:
                right=med-1
            else:
                left=med+1
        return -1

nums = [-1,0,3,5,9,12]
target = 9
print(search(nums,target))