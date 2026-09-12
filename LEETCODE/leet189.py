def rotate(nums, k):
        n = len(nums)
        k = k % n

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Step 1: Reverse everything -> [7,6,5,4,3,2,1]
        reverse(0, n - 1)
        # Step 2: Reverse first k elements -> [5,6,7,4,3,2,1]
        reverse(0, k - 1)
        # Step 3: Reverse remaining elements -> [5,6,7,1,2,3,4]
        reverse(k, n - 1)
        return nums

nums = [1,2,3,4,5,6,7]
k = 3

print(rotate(nums,k))