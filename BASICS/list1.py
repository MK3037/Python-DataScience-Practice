list1=[1,2,"python","goood"]
list2=["hi","hello"]

for colour in list2:
    print(colour)
    for i in colour:
        print(i)

print(list1)
print(type(list2))
list1[1]=9
print(list1[0]+list1[-3])
x=list1.index(1)
list1.append((999))
list1.insert(0,90)
list1.extend(list2)     #or do list4=list1+list2
print(list1)
print(x,"\n")

list3=list(range(5))
print(list3)
list3.pop()
list3.remove(2)
list3.insert(10,2)
print(list3)
del list3[1:3]
print(list3)
list3.clear()


arr = [10, 20, 30, 40, 50, 60]
print(arr[1:4])      # [20, 30, 40] -> Elements from index 1 up to (but excluding) 4
print(arr[:3])       # [10, 20, 30] -> Elements from the beginning up to index 3
print(arr[::2])      # [10, 30, 50] -> Elements from start to end, skipping by a step of 2


