# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy (sentinel) node to simplify the logic
        dummy = ListNode(0)
        ptr = dummy
        carry = 0
        
        # Loop until both lists are empty and there is no remaining carry 
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and carry
            total_sum = val1 + val2 + carry
            carry = total_sum // 10
            new_val = total_sum % 10
            
            # Add the new digit to the result list 
            ptr.next = ListNode(new_val)
            
            # Move pointers forward
            ptr = ptr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next

# --- Helper code to run the solution in VS Code ---

def list_to_linkedlist(lst):
    dummy = ListNode(0)
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

if __name__ == "__main__":
    # Test Case: 243 + 564 (342 + 465 = 807) -> Result should be [7, 0, 8]
    l1 = list_to_linkedlist([2, 4, 3])
    l2 = list_to_linkedlist([5, 6, 4])
    
    sol = Solution()
    res = sol.addTwoNumbers(l1, l2)
    
    print(f"Result: {linkedlist_to_list(res)}")