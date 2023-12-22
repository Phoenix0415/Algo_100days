import sys # import sys module
from pathlib import Path # import Path object from pathlib module

sys.path.append(str(Path(__file__).parent.parent)) # add parent path to sys.path
from modules import TreeNode, print_tree # import modules from parent path

"""Driver Code"""
if __name__ == "__main__":
    # initialize binary tree
    # 1. initialize nodes
    n1 = TreeNode(val=1)
    n2 = TreeNode(val=2)
    n3 = TreeNode(val=3)
    n4 = TreeNode(val=4)
    n5 = TreeNode(val=5)
    # 2. initialize connections
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    print("\ninitialize binary tree\n")
    print_tree(n1)

    # insert and delete node
    P = TreeNode(0)
    # insert node P bewteen n1 and n2
    n1.left = P
    P.left = n2
    print("\nafter insert node P\n")
    print_tree(n1)
    # delete node P
    n1.left = n2
    print("\nafter delete node P\n")
    print_tree(n1)