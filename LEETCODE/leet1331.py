def arrayRankTransform(arr):
        x=arr[:]
        x.sort()
        freq={}
        count=0

        for i in range(len(x)):
            if x[i] not in freq:
                count+=1
            freq[x[i]]=count

        return [freq[y] for y in arr]

print(arrayRankTransform([40,10,20,30]))