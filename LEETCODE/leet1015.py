class Solution(object):
    def smallestRepunitDivByK(self, k):
        if k%2==0 or k%5==0:        #as 11 or 111 or any such number wouldnt be even so we used 2,
            return -1               #and to be divisible by 5 it should end with 5 or 0 which isnt the case either.
                                    #So we did it to improve efficiency 
        num=0
        for i in range(1,k+1):  #as it doesnt include k+1 and goes till k onlt=y
            num=num*10+1
            if num%k==0:
                return i
        return -1
    
x=Solution()
print(x.smallestRepunitDivByK(7))