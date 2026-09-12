class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        currentnode=head
        length=0
        while currentnode is not None:
            currentnode=currentnode.next
            length+=1
        if length==n:
            return head.next
        currentnode=head
        for i in range(length-n-1):
            currentnode=currentnode.next
        if currentnode.next is not None:
            currentnode.next=currentnode.next.next
        return head