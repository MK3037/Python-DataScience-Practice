gain = [-5,1,5,0,-7]
altitudes=[]
current=0
for i in range(len(gain)):
    altitudes.append(current)
    current+=gain[i]            #as loop exits here, last current calculated isnt appended which was expected to happen in next loop           
        
altitudes.append(current)
print(max(altitudes))



        # h=0
        # max=0
        # for p in range(len(gain)):
        #     h+=gain[p]
        #     if h>max:
        #         max=h
        # return max                    move, add, compare with max