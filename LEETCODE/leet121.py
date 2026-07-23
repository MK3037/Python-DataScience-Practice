a=[7,1,5,3,6,4]
profit=0
buy=0
sell=1

while sell!=len(a)-1:
    if a[buy+1]<a[buy]:
        buy+=1
    if a[sell]<a[sell+1]:
        sell+=1
    pro=a[sell]-a[buy]
    if pro>profit:
        profit=pro
    sell+=1
print(profit)



# for buy in range(len(a)):
#     for sell in range(buy+1,len(a)):
#         pro=a[sell]-a[buy]
#         if pro>profit:
#             profit=pro
# print(profit)