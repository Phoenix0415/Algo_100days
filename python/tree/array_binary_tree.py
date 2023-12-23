import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from modules import TreeNode, list_to_tree, print_tree

class ArrayBinaryTree:
    """binary tree in array representation"""

    def __init__(self, arr: list[int | None]):
        """constructor"""
        self._tree = list(arr)

    def size(self):
        """the number of nodes in the tree"""
        return len(self._tree)

    def val(self, i: int) -> int:
        """get the value of the node at index i"""
        # if the index is out of range, return None
        if i < 0 or i >= self.size():
            return None
        return self._tree[i]

    def left(self, i: int) -> int | None:
        """get the value of the left child of the node at index i"""    
        return 2 * i + 1

    def right(self, i: int) -> int | None:
        """get the value of the right child of the node at index i"""
        return 2 * i + 2

    def parent(self, i: int) -> int | None:
        """get the index of the parent of the node at index i"""
        return (i - 1) // 2

    def level_order(self) -> list[int]:
        """level order traversal"""
        self.res = []
        # traverse the tree directly
        for i in range(self.size()):
            if self.val(i) is not None:
                self.res.append(self.val(i))
        return self.res

    def dfs(self, i: int, order: str):
        """depth first traversal"""
        if self.val(i) is None:
            return
        # pre-order traversal
        if order == "pre":
            self.res.append(self.val(i))
        self.dfs(self.left(i), order)
        # in-order traversal
        if order == "in":
            self.res.append(self.val(i))
        self.dfs(self.right(i), order)
        # post-order traversal
        if order == "post":
            self.res.append(self.val(i))

    def pre_order(self) -> list[int]:
        """pre-order traversal"""
        self.res = []
        self.dfs(0, order="pre")
        return self.res

    def in_order(self) -> list[int]:
        """in-order traversal"""
        self.res = []
        self.dfs(0, order="in")
        return self.res

    def post_order(self) -> list[int]:
        """post-order traversal"""
        self.res = []
        self.dfs(0, order="post")
        return self.res


"""Driver Code"""
if __name__ == "__main__":
    # inirialize a binary tree
    # use function list_to_tree() to convert an array to a tree
    arr = [1, 2, 3, 4, None, 6, 7, 8, 9, None, None, 12, None, None, 15]
    root = list_to_tree(arr)
    print("\ninitialize a binary tree:")
    print("the array representation of the tree:")
    print(arr)
    print("the linked list representation of the tree:")
    print_tree(root)

    # the array representation of the tree
    abt = ArrayBinaryTree(arr)

    # get the value of the nodes
    i = 1
    l, r, p = abt.left(i), abt.right(i), abt.parent(i)
    print(f"\nthe index of the node is {i} , value is {abt.val(i)}")
    print(f"the index of its left child is {l} , value is {abt.val(l)}")
    print(f"the index of its right child is {r} , value is {abt.val(r)}")
    print(f"the index of its parent is {p} , value is {abt.val(p)}")

    # tree traversal
    res = abt.level_order()
    print("\nlevel order traversal:", res)
    res = abt.pre_order()
    print("pre-order traversal:", res)
    res = abt.in_order()
    print("in-order traversal:", res)
    res = abt.post_order()
    print("post-order traversal:", res)