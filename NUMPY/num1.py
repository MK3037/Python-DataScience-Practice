import time
import numpy as np
a=[1,2,3,4,5]
b=[1,2,3,4,5]

start=time.time()
c=[a+b for a,b in zip(a,b)]
print(c)
end=time.time()
print(end-start)                                #more time and space almost 10-20x

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 3, 4, 5])

start=time.time()
z=x+y
print(z)
end=time.time()
print(end-start)                                #lesser time and space

print([x*x for x in a])                         #have to loop in list
print(f'{x**2}\n')                                     #no need in numpy

d=np.zeros((2,3))
d=np.ones((2,2))
d=np.full((2,3),7)
d=np.arange(1,10,2)
d=np.arange(3)
d=np.linspace(0, 10, num=5)
print(f'{d}\n')

myarray=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(myarray)
print(myarray.size)
print(myarray.shape)
print(myarray.ndim)
print(myarray[2,1])
myarray=myarray.reshape((2,6))
print(myarray)
myarray=myarray.flatten()
print(myarray)

#SEE LIST1 FILE TO RECALL INDEXING AND SLICING, SAME IN NUMPY AND ARRAY ALSO
# num_arr = np.array([1, 2, 3, 4, 5])
# my_view = num_arr[1:4]  # Slicing a NumPy array creates a view, not a copy
# my_view[0] = 99         # Changing the slice affects index 1 of the original array
# print(num_arr)          # Output: [1, 99, 3, 4, 5]
#THIS IS ONLY DIFFERENCE , IN NUMPY CHANGING THE SLICING WOULD ALSO CHANGE THE MAIN ARRAY
#CHANGING MYVIEW WHICH WAS SLICED FROM NUM_ARR ALSO CHANGED NUM_ARR

#TO MAKE A COPY USE 
# my_view = num_arr[1:4].copy()     #BUT NOW ITS NOT SLICE