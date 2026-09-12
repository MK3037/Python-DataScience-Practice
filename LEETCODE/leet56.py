def merge(intervals):
        i=0
        intervals.sort(key=lambda x:x[0])
        print(intervals)
        while i in range(len(intervals)):
            if i!=len(intervals)-1 and intervals[i][1]>=intervals[i+1][0]:
                intervals[i+1]=([intervals[i][0],intervals[i+1][1]])
                intervals.pop(i)
                continue
            i+=1
        return intervals
intervals = [[1,3],[1,6],[2,10],[15,18]] 
print(merge(intervals))
