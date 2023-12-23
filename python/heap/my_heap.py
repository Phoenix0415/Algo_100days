import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from modules import print_heap


class MaxHeap:
    """max-heap"""

    def __init__(self, nums: list[int]):
        """constructor, heapify nums"""
        # push all elements to heap by original order 
        self.max_heap = nums
        # heapify from bottom to top except leaf nodes
        for i in range(self.parent(self.size() - 1), -1, -1):
            self.sift_down(i)

    def left(self, i: int) -> int:
        """get index of left child node"""
        return 2 * i + 1

    def right(self, i: int) -> int:
        """get index of right child node"""
        return 2 * i + 2

    def parent(self, i: int) -> int:
        """get index of parent node"""
        return (i - 1) // 2  # floor division

    def swap(self, i: int, j: int):
        """swap two nodes"""
        self.max_heap[i], self.max_heap[j] = self.max_heap[j], self.max_heap[i]

    def size(self) -> int:
        """get size of heap"""
        return len(self.max_heap)

    def is_empty(self) -> bool:
        """check if heap is empty"""
        return self.size() == 0

    def peek(self) -> int:
        """get top element of heap"""
        return self.max_heap[0]

    def push(self, val: int):
        """push element to heap"""
        # add element to heap
        self.max_heap.append(val)
        # heapify from bottom to top
        self.sift_up(self.size() - 1) # size - 1 is the index of last element

    def sift_up(self, i: int):
        """heapify from bottom to top, from leaf node i to root"""
        while True:
            # get index of parent node
            p = self.parent(i)
            # when the index of parent node is out of range or node i is smaller than its parent node, stop heapify
            if p < 0 or self.max_heap[i] <= self.max_heap[p]:
                break
            # swap node i and its parent node
            self.swap(i, p)
            # continue heapify to top
            i = p

    def pop(self) -> int:
        """pop element of heap"""
        # check if heap is empty
        if self.is_empty():
            raise IndexError("the heap is empty")
        # swap root and rightmost leaf node in heap(or last and first element in list)
        self.swap(0, self.size() - 1)
        # delete last element
        val = self.max_heap.pop()
        # heapify from top to bottom
        self.sift_down(0)
        # return top element
        return val

    def sift_down(self, i: int):
        """heapify from top to bottom, from node i to leaf nodes"""
        while True:
            # find max node among node i and its left and right child nodes l, r, and record its index ma
            l, r, ma = self.left(i), self.right(i), i
            # if l is in range and node l is larger than node ma, update ma
            if l < self.size() and self.max_heap[l] > self.max_heap[ma]:
                ma = l
            # if r is in range and node r is larger than node ma, update ma
            if r < self.size() and self.max_heap[r] > self.max_heap[ma]:
                ma = r
            # when the index of child node is out of range or node i is larger than its child nodes, stop heapify
            if ma == i:
                break
            # swap node i and max node
            self.swap(i, ma)
            # continue heapify to bottom
            i = ma

    def print(self):
        """print heap(binary tree)"""
        print_heap(self.max_heap)


"""Driver Code"""
if __name__ == "__main__":
    # initialize max-heap
    max_heap = MaxHeap([9, 8, 6, 6, 7, 5, 2, 1, 4, 3, 6, 2])
    print("\ninitialize list as max-heap")
    max_heap.print()

    # get the top element of heap
    peek = max_heap.peek()
    print(f"\nthe top element is {peek}")

    # push element to heap
    val = 7
    max_heap.push(val)
    print(f"\nafter push {val} into heap")
    max_heap.print()

    # pop top element of heap
    peek = max_heap.pop()
    print(f"\nafter pop {peek} out of heap")
    max_heap.print()

    # get the size of heap
    size = max_heap.size()
    print(f"\nget the size of heap {size}")

    # check if heap is empty
    is_empty = max_heap.is_empty()
    print(f"\nwhether the heap is empty {is_empty}")