'''The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array'''
def majorityElement(nums):
        count={}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num, cnt in count.items():
            if cnt > len(nums)//2:
                return num 

print(majorityElement([2,2,1,1,1,2,2]))