num=[1,2,5,6]
target=4                #or any big number it would be at len(a)+1 only. so no problem with that 
i=0

found=False
while i <len(num) and num[i]<=target:
    if target==num[i]:
        print("its at",i+1,"position")
        found=True
    i=1+i
if found==False:
    print("it should be at",i+1,"position")