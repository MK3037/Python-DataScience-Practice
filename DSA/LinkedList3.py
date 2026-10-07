class node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def traverse(head):
        currenthead=head
        while currenthead:
            print(currenthead.data, end="->")
            currenthead=currenthead.next
        print("None")

    def insertatbegining(head,x):
        newnode=node(x)
        newnode.next=head
        return newnode

    def insertatend(head,x):
        newnode=node(x)
        if head is None:
            return newnode
        currentnode=head
        while currentnode.next is not None:
            currentnode=currentnode.next
        currentnode.next=newnode
        return head
    
    def insertatn(head,x,n):
        if n==0:
            node.insertatbegining(head,x)
        newnode=node(x)                             #traverse
        currentnode=head    
        for i in range(n-1):
            currentnode=currentnode.next                
        newnode.next=currentnode.next
        currentnode.next=newnode                   
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
node.traverse(head_node)

head_node=node.insertatbegining(head_node,4)
print(node.traverse(head_node))

head_node=node.insertatend(head_node,4)
print(node.traverse(head_node))

head_node=node.insertatn(head_node,10,3)
print(node.traverse(head_node))