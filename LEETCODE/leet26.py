'''Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.'''
def removeDuplicates(nums):
        i=0
        j=1
        while j<len(nums):
            if nums[j]>nums[i]:
                i+=1
                nums[i]=nums[j]
            j+=1
        return i+1

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))