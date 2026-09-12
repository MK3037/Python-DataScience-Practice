def solveQueries(nums, queries):
        n=len(nums)
        ans=[]
        for i in queries:
            shortest=float('inf')
            for j in range(i+1,n+i):
                y=j%n
                if nums[y]==nums[i]:
                    step = j - i                #hard to understand and was given by ai
                    distance = min(step, n - step)  #this is with above 
                    shortest=min(shortest,distance)
            if shortest!=float('inf'):
                ans.append(shortest)
            else:
                ans.append(-1)
        return ans

#time limit excedded else correct

ums = [1,3,1,4,1,3,2]
queries = [0,3,5]
print(solveQueries(ums,queries))