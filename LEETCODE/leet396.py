nums = [4,3,2,6]
i=len(nums)             #4
nums.extend(nums)       #nums= [4, 3, 2, 6, 4, 3, 2, 6]
j=len(nums)             #8

max=0
while i!=0:
    a=0
    total=0
    for k in range(i,j):
        total=(a*nums[k])+total
        a+=1
    if total>max:
        max=total
    i-=1
    j-=1
print(max)
