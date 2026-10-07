class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

DFS=[]                                      #Depth first search or iterative traversal is same as this inordertraversal.
def inOrderTraversal(node):                 #DFS is implemented using stack
    if not node:
        return
    inOrderTraversal(node.left)
    DFS.append(node.val)
    inOrderTraversal(node.right)

# Creating nodes for the tree
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node10 = TreeNode(10)

# Connecting the nodes to form a binary tree structure
node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node3.left = node10

# Running the pre-order traversal starting from the root (node1)
inOrderTraversal(node1)
print(DFS)


#1. What is DFS?Depth-First Search is an overarching strategy that visits a branch as deep as possible before backtracking. 
# In a binary tree, all three standard traversal strategies are forms of DFS:
# Pre-order DFS (Root $\rightarrow$ Left $\rightarrow$ Right): [1, 2, 4, 5, 3, 10]
# In-order DFS (Left $\rightarrow$ Root $\rightarrow$ Right): [4, 2, 5, 1, 10, 3]
# Post-order DFS (Left $\rightarrow$ Right $\rightarrow$ Root): [4, 5, 2, 10, 3, 1]