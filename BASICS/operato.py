a='''Python divides the operators in the following groups:

Arithmetic operators            #same as c and c++                                  +,-,*,%,/,**,//
Assignment operators            #same as c and c++                                  =,+=,-=,**=,>>=and many more
Comparison operators            #same as c and c++                                  ==,!=,>,<,>=,<=
Logical operators               #different from c and c++.                          and-&&  or-||  not-!
Identity operators              #something new
Membership operators            #something new
Bitwise operators               #same as c and c++
'''

#ARITHMATIC OPERATOR
print(10**2)        #Exponentiatioal
print(10//2)        #Floor function

#LOGICAL OPERATOR
x=int(input('Enter a number: '))
y=int(input('Enter another number: '))
print(x>=1 and y>=1)                #Returns True if both statements are true
print(x<=1 or y<=1)                 #Returns True if one of the statements is true
print(not(x < 5 and x < 10))        #Reverse the result, returns False if the result is true

#IDENTITY OPERATOR
print()
b,c=2,3
print(b is c)                       #Return true if both variables are same
print(b is not c)                   #Return true if both variables arent same
 # type: ignore