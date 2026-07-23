def numOfSubarrays(arr, k, threshold):
        count=0
        sums=sum(arr[i] for i in range(k))
        if sums/k>=threshold:
            count+=1
        
        for i in range(k, len(arr)):
            sums+=arr[i]
            sums-=arr[i-k]          #or sums=sums+arr[i]-arr[i-k]
            if sums/k>=threshold:
                count+=1
        return count
arr=[2,2,2,2,5,5,5,8]
k=3
threshold=4
print(numOfSubarrays(arr,k,threshold))