class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        currentnode = dummy

        while currentnode.next and currentnode.next.next:
            first = currentnode.next
            second = currentnode.next.next

            temp = second.next         
            currentnode.next = second  
            second.next = first      
            first.next = temp        

            currentnode = first      

        return dummy.next