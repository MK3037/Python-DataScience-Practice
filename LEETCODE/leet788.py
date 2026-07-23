def rotatedDigits(n):
        count=0
        for j in range(1,n+1):
            good=False
            while j!=0:
                i=j%10
                j=j//10

                if i==3 or i==4 or i==7:
                    good=False
                    break
                elif i==2 or i ==5 or i==6 or i==9:
                    good=True
            if good==True:
                count+=1
        return count


y=rotatedDigits(857)
print(y)