def merge(intervals):
        i=0
        intervals.sort(key=lambda x:x[0])
        print(intervals)
        while i in range(len(intervals)-1):
            if intervals[i][1]>=intervals[i+1][0]:
                x=max(intervals[i+1][1],intervals[i][1])
                intervals[i+1]=([intervals[i][0],x])
                intervals.pop(i)
                continue
            i+=1
        return intervals
intervals = [[1,3],[1,6],[2,10],[15,18]] 
intervals = [[1, 4], [2, 3]]
print(merge(intervals))
