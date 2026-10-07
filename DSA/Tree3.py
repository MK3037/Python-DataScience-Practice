class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs_traversal(root):
    if not root:
        return []
    
    result = []
    queue = [root]  # Standard list as queue
    
    while queue:
        # Pop the first node in the queue (FIFO order)
        current = queue.pop(0)
        result.append(current.val)
        
        # Enqueue left child then right child
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
            
    return result


# --- Recreating your exact tree setup ---
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node10 = TreeNode(10)

node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node3.left = node10

# --- Output ---
print(bfs_traversal(node1))  # [1, 2, 3, 4, 5, 10]