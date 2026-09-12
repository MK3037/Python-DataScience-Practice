class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        currentnode=head    
        leng=0
        while currentnode:
            currentnode=currentnode.next
            leng+=1
        currentnode=head
        for i in range(leng//2):
            currentnode=currentnode.next
        return currentnode

