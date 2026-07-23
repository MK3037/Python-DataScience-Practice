nums = [0,4,3,0,4]
for i in range(1,len(nums)+1):
    count=0
    for j in nums:
        if j>=i:
            count+=1
    if count==i:
        print(i)