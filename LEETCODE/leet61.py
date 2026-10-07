# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if head==None or head.next==None:
            return head
        currentnode=head
        length=1
        while currentnode.next:
            currentnode=currentnode.next
            length+=1

        k %= length
        if k == 0:
            return head

        currentnode.next=head
        currentnode=currentnode.next

        for i in range(length-k):               #cant get why length-k and not k
            currentnode=currentnode.next
        lastnode=currentnode
        for i in range(length-1):
            lastnode=lastnode.next
        lastnode.next=None
        return currentnode