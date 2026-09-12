class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

def preOrderTraversal(node):
    if not node:
        return
    # Process/print the current node
    print(node.val)
    # Traverse left
    preOrderTraversal(node.left)
    # Traverse right
    preOrderTraversal(node.right)

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
preOrderTraversal(node1)