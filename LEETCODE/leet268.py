nums = [3,0,1]
total=0
for i in nums:
    total=total+i                                   #total of all given number from 0 to n with one missing

x=max(nums)
sum = x*(x+1)/2                                     #total of all number form 0 to n
ans=sum-total                                       #subtracting would give that missing number 
print(ans)