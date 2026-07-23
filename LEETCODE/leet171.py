'''Given a string columnTitle that represents the column title as appears in an Excel sheet, 
return its corresponding column number'''
num=[0]*26
for i in range (len(num)):
    num[i]=i+1
print(num)
alphabet = list("abcdefghijklmnopqrstuvwxyz")
print(alphabet)

inp=list(input("enter the columnnumber: "))

result=int(0)
for i in inp:
    x=alphabet.index(i)
    result=26*result+num[x]

print(result)