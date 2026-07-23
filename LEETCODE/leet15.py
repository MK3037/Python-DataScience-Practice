a=[1,2,3,-1,-2]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        for k in range(j+1,len(a)):
            if a[i]+a[j]+a[k]==0 and i!=j and i!=k and j!=k :
                print(i+1,j+1,k+1)
                print(a[i],a[j],a[k])
                break