'''Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn]'''
x=[1,2,3,4,5,6]
n=3
result=[]
for i,j in zip(x[:n],x[n:]):
    result.extend([i,j])
print(result)