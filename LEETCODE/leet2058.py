# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        count=0
        critical=[]
        currentnode=head
        while currentnode.next.next is not None:
            count+=1
            if currentnode.next.val<currentnode.val and currentnode.next.val<currentnode.next.next.val:
                critical.append(count+1)
            if currentnode.next.val>currentnode.val and currentnode.next.val>currentnode.next.next.val:
                critical.append(count+1)
            currentnode=currentnode.next
        if len(critical) < 2:
            return [-1, -1]
        maxDistance=critical[-1]-critical[0]
        minDistance=min(critical[i]-critical[i-1] for i in range(1,len(critical)))
        return [minDistance,maxDistance]