def maxDepth(s):
        depth=0
        maxdepth=0
        for i in s:
            if i=='(':
                depth+=1
            elif i==')':
                maxdepth=max(maxdepth,depth)
                depth-=1
        return maxdepth

s = "(1+(2*3)+((8)/4))+1"
print(maxDepth(s))