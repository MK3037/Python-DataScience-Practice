class node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def traverse(head):
        currenthead=head
        while currenthead:
            print(currenthead.data)
            currenthead=currenthead.next

def createlinkedlist(arr):
    head=node(arr[0])
    current=head
    for items in arr[1:]:
        current.next=node(items)
        current=current.next
    return head


Mylist=[2,3,4,5,6]
head_node = createlinkedlist(Mylist)
print(node.traverse(head_node))