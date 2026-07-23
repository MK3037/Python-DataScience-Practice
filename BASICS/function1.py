def find_square(num):                   #with return value
    result=num**2
    return result
x=int((input("enter")))
square = find_square(x)
print('square:',square)

#LAMBDA
squa = lambda x: x*x                    #defining a function in a line
print(f"lambda: {squa(2)} ")                          #also called lambda function

avg = lambda x,y,z: (x+y+z)/3
print(f"lambda: {avg(1,2,3)}")

#MAP
l=[1,2,3,4,5,6,7,8,9]                   #newl=[]                    thats make a new list newl with applied function
newl=list(map(squa,l))                  #for item in l:             squa to each element of old funcion l
print(f"map: {newl}")                             #   newl.append(squa(item)) 
newl=list(map(lambda x:x*x*x,l))
print(f"map: {newl}")

#FILTER
def filter_function(a):
    return a>4
newl=list(filter(filter_function,l))
print(f"filter: {newl}")

#REDUCE
from functools import reduce
def sum(num1,num2):                     
    return num1+num2
sum1=reduce(sum,l)
print(f"reduce: {sum1}")

#ZIP
names = ["Alice", "Bob", "Charlie","mihir"]
scores = [85, 92, 78]
mydict={}
combined = zip(names, scores)
print(list(combined))
for names,scores in zip(names,scores):
    mydict[names]=scores
print(mydict)
def hi():
    return "yo"
print(hi().upper())