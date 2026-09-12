class node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def traverse(head):
        currenthead=head
        while currenthead:
            print(currenthead.data,end="->")
            currenthead=currenthead.next
        print("None")

    def deletefirst(head):
        currentnode=head
        currentnode=currentnode.next
        return currentnode

    def deletelast(head):
        currentnode=head
        while currentnode.next.next is not None:
            currentnode=currentnode.next 
        currentnode.next=None
        return head

    def deleteatn(head,n):
        currentnode=head
        for i in range(n-1):
            currentnode=currentnode.next
        if currentnode.next is not None:
            currentnode.next = currentnode.next.next
        return head 
        
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

head_node=node.deletefirst(head_node)
print(node.traverse(head_node))

head_node=node.deletelast(head_node)
print(node.traverse(head_node))

head_node=node.deleteatn(head_node,2)
print(node.traverse(head_node))