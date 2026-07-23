n=12
ans=[]


for i in range(1,n+1):
    if n%i==0:
        ans.append(i)
print(f"FACTORS USING BRUTE FORCE: {ans}")

i=1
ans.clear()
while i*i<=n:
    if (n%i==0):
        ans.append(i)
        if (i!=n//i):               #to avoid adding 4 twice in case of n=16(perfect number case)
            ans.append(n//i)
    i+=1
print(f"FACTORS USING OPTIMIZED WAY: {ans}")