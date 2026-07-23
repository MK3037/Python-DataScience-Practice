def sumAndMultiply(s, queries):
        MOD = 10**9 + 7
        ans=[]
        x=0

        for i in queries:
            x=[s[j] for j in range(i[0],i[1]+1) if s[j]!='0']
            sums=sum(int(i) for i in x)
            if x: 
                val = int("".join(x))
                ans.append((val * sums) % MOD)
            else:
                ans.append(0) 
        return ans

print(sumAndMultiply('10203004',[[0,7],[1,3],[4,6]]))