import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from modules import TreeNode, list_to_tree, print_tree
from collections import deque


def level_order(root: TreeNode | None) -> list[int]:
    """level order traversal of a binary tree"""
    # initialize a queue, and append root node
    queue: deque[TreeNode] = deque()
    queue.append(root)
    # initialize a list to store node values
    res = []
    while queue:
        node: TreeNode = queue.popleft()  # dequeue a node
        res.append(node.val)  # store node value in res list
        if node.left is not None:
            queue.append(node.left)  # enqueue left child node
        if node.right is not None:
            queue.append(node.right)  # enqueue right child node
    return res


"""Driver Code"""
if __name__ == "__main__":
    # initialize a binary tree
    # here we use a function to generate a binary tree from an array
    root: TreeNode = list_to_tree(arr=[1, 2, 3, 4, 5, 6, 7])
    print("\ninitialize a binary tree\n")
    print_tree(root)

    # level order traversal
    res: list[int] = level_order(root)
    print("\nthe level order traversal of the binary tree = ", res)