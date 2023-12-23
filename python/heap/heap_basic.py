import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from modules import print_heap

import heapq


def test_push(heap: list, val: int, flag: int = 1):
    heapq.heappush(heap, flag * val)  # push element into heap
    print(f"\nafter push element {val} into heap")
    print_heap([flag * val for val in heap]) # list comprehension


def test_pop(heap: list, flag: int = 1):
    val = flag * heapq.heappop(heap)  # pop element from top of heap
    print(f"\nafter pop element {val} from the top of heap")
    print_heap([flag * val for val in heap])


"""Driver Code"""
if __name__ == "__main__":
    # initialize a min heap
    min_heap, flag = [], 1 # assign min_heap to [], flag = 1 for min heap, using tuple unpacking
    # initialize a max heap
    max_heap, flag = [], -1

    print("\nthe following tests are for max heap")
    # the default heapq in python is min heap
    # to build a max heap, we need to multiply -1 to each element
    # here, we use flag to control the sign of each element, flag = -1 for max heap, flag = 1 for min heap

    # push elements into heap
    test_push(max_heap, 1, flag)
    test_push(max_heap, 3, flag)
    test_push(max_heap, 2, flag)
    test_push(max_heap, 5, flag)
    test_push(max_heap, 4, flag)

    # get the top element of heap
    peek: int = flag * max_heap[0]
    print(f"\nthe top element is {peek}")

    # pop elements from top of heap
    test_pop(max_heap, flag)
    test_pop(max_heap, flag)
    test_pop(max_heap, flag)
    test_pop(max_heap, flag)
    test_pop(max_heap, flag)

    # get the size of heap
    size: int = len(max_heap)
    print(f"\nthe size of the heap is {size}")

    # check if heap is empty
    is_empty: bool = not max_heap
    print(f"\nif the heap is empty: {is_empty}")

    # initialize a list and build a min heap
    # the time complexity of building a heap is O(n). not O(nlogn)
    min_heap = [1, 3, 2, 5, 4]
    heapq.heapify(min_heap)
    print("\nafter heapify")
    print_heap(min_heap)
    