def findMaxAverage(nums, k):
        intialsum = float(sum(nums[i] for i in range(k)))

        maxsum=intialsum
        
        for i in range(k,len(nums)):
            intialsum += nums[i]
            intialsum -= nums[i-k]

            maxsum=max(intialsum,maxsum)

        return maxsum/k


print(findMaxAverage([1,12,-5,-6,50,3],4))

