def pivotIndex(self, nums):
        total = sum(nums)
        leftsum = 0
        for i, n in enumerate(nums):
            if leftsum == total - leftsum - n:
                return i
            leftsum += n
        return -1

nums = [1,7,3,6,5,6]
print(pivotIndex(nums))