def maxProduct(n):
        x=list(str(n))
        x.sort()
        return int(x[-1])*int(x[-2])

# 10 <= n <= 109
print(maxProduct(31))