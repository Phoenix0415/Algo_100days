import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from modules import TreeNode, print_tree


class BinarySearchTree:
    """binary search tree"""

    def __init__(self):
        """constructor"""
        # initialize the root node
        self._root = None

    def get_root(self) -> TreeNode | None:
        """get the root node"""
        return self._root

    def search(self, num: int) -> TreeNode | None:
        """search the node with the given value"""
        cur = self._root
        # using loop to find the target node, and break when the target node is found
        while cur is not None:
            # the target node is in the right subtree of cur node
            if cur.val < num:
                cur = cur.right
            # the target node is in the left subtree of cur node
            elif cur.val > num:
                cur = cur.left
            # the target node is found, break the loop
            else:
                break
        return cur

    def insert(self, num: int):
        """insert a node with the given value"""
        # if the tree is empty, initialize the root node
        if self._root is None:
            self._root = TreeNode(num)
            return
        # using loop to find the insert position, and break when the insert position is found
        cur, pre = self._root, None
        while cur is not None:
            # find the insert position, break the loop
            if cur.val == num:
                return
            pre = cur
            # the insert position is in the right subtree of cur node
            if cur.val < num:
                cur = cur.right
            # the insert position is in the left subtree of cur node
            else:
                cur = cur.left
        # insert the node
        node = TreeNode(num)
        if pre.val < num:
            pre.right = node
        else:
            pre.left = node

    def remove(self, num: int):
        """delete the node with the given value"""
        # if the tree is empty, return directly
        if self._root is None:
            return
        # if the root node is the target node, delete the root node
        cur, pre = self._root, None
        while cur is not None:
            # if the target node is found, break the loop
            if cur.val == num:
                break
            pre = cur
            # if the target node is in the right subtree of cur node
            if cur.val < num:
                cur = cur.right
            # if the target node is in the left subtree of cur node
            else:
                cur = cur.left
        # if the target node is not found, return directly
        if cur is None:
            return

        # the number of subtree nodes is 0 / 1
        if cur.left is None or cur.right is None:
            # when the number of subtree nodes is 0/1, child = null / the only child node
            child = cur.left or cur.right
            # delete the cur node
            if cur != self._root:
                if pre.left == cur:
                    pre.left = child
                else:
                    pre.right = child
            else:
                # if to be deleted is the root node, then the child node is the new root node
                self._root = child
        # if the number of subtree nodes is 2
        else:
            # get the leftmost node of the right subtree
            tmp: TreeNode = cur.right
            while tmp.left is not None:
                tmp = tmp.left
            # delete tmp recursively
            self.remove(tmp.val)
            # using tmp to replace cur
            cur.val = tmp.val


"""Driver Code"""
if __name__ == "__main__":
    # initialize the binary search tree
    bst = BinarySearchTree()
    nums = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    # note: the order of inserting nodes will affect the shape of the binary search tree
    for num in nums:
        bst.insert(num)
    print("\nthe initial binary search tree is\n")
    print_tree(bst.get_root())

    # search the node with the given value
    node = bst.search(7)
    print("\nthe node with value 7 is: {}, the value = {}".format(node, node.val))

    # insert a node with the given value
    bst.insert(16)
    print("\nafter inserting a node with value 16, the binary search tree is\n")
    print_tree(bst.get_root())

    # delete the node with the given value
    bst.remove(1)
    print("\nafter deleting a node with value 1, the binary search tree is\n")
    print_tree(bst.get_root())

    bst.remove(2)
    print("\nafter deleting a node with value 2, the binary search tree is\n")
    print_tree(bst.get_root())

    bst.remove(4)
    print("\nafter deleting a node with value 4, the binary search tree is\n")
    print_tree(bst.get_root())