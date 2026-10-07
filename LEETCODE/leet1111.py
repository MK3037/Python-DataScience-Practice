def maxDepthAfterSplit(seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        depth=[]
        d=0
        for i in seq:
            if i=='(':
                depth.append(d%2)   # eariler was also correct, but we have to assign 0,1 only so for alternate effect we do modulo. else depth finding and then modulo is what was remaining.
                d+=1
            else:
                d-=1
                depth.append(d%2)
        return depth

s="((()))"
print(maxDepthAfterSplit(s))