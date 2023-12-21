class TreeNode:
    """brinary tree node class"""
    def __init__(self, val: int):
        self.val: int = val                # the value of the node
        self.left: TreeNode | None = None  # left child node reference
        self.right: TreeNode | None = None # right child node reference
        
def main():
    # initialize binary tree
    # step1: initialize nodes
    n1 = TreeNode(val=1)
    n2 = TreeNode(val=2)
    n3 = TreeNode(val=3)
    n4 = TreeNode(val=4)
    n5 = TreeNode(val=5)
    # step2: set relationships between nodes
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5

if __name__ == '__main__':
    main()