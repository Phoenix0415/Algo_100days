import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from modules import TreeNode, list_to_tree, print_tree

def pre_order(root: TreeNode | None):
    """pre-order traversal of a binary tree"""
    if root is None:
        return
    # the order of visiting nodes: root -> left subtree -> right subtree
    res.append(root.val)
    pre_order(root=root.left)
    pre_order(root=root.right)


def in_order(root: TreeNode | None):
    """in-order traversal of a binary tree"""
    if root is None:
        return
    # the order of visiting nodes: left subtree -> root -> right subtree
    in_order(root=root.left)
    res.append(root.val)
    in_order(root=root.right)


def post_order(root: TreeNode | None):
    """post-order traversal of a binary tree"""
    if root is None:
        return
    # the order of visiting nodes: left subtree -> right subtree -> root
    post_order(root=root.left)
    post_order(root=root.right)
    res.append(root.val)


"""Driver Code"""
if __name__ == "__main__":
    # initailize a binary tree
    # 这里借助了一个从数组直接生成二叉树的函数
    root = list_to_tree(arr=[1, 2, 3, 4, 5, 6, 7])
    print("\ninitialize a binary tree\n")
    print_tree(root)

    # pre-order traversal
    res = []
    pre_order(root)
    print("\npre-order traversal of the binary tree = ", res)

    # in-order traversal
    res.clear()
    in_order(root)
    print("\nin-order traversal of the binary tree = ", res)

    # post-order traversal
    res.clear()
    post_order(root)
    print("\npost-order traversal of the binary tree = ", res) 