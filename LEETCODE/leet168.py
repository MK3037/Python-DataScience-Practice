'''Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet'''
num=list(range(1,27))
print(num)
alphabet = list("abcdefghijklmnopqrstuvwxyz")
print(alphabet)

inp=int(input('enter the number:'))

while inp!=0:
    x=inp%26
    inp=inp//26
    print(alphabet[x-1])  #would print in reverse. thats ba instead of ab. solve it by storing and reversing when free