def subarraySum(nums, k):
    prefix_counts = {0: 1}
    prefix_sum = 0
    ans = 0 

    for num in nums:
        prefix_sum += num
        ans += prefix_counts.get(prefix_sum - k, 0)
        prefix_counts[prefix_sum] = prefix_counts.get(prefix_sum, 0) + 1
        
    return ans

test_nums1 = [1, 1, 1]
test_k1 = 2
print(f"Result 1: {subarraySum(test_nums1, test_k1)}")  # Expected output: 2


test_nums2 = [1, 2, 3]
test_k2 = 3
print(f"Result 2: {subarraySum(test_nums2, test_k2)}")  # Expected output: 2