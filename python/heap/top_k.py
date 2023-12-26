import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from modules import print_heap

import heapq


def top_k_heap(nums: list[int], k: int) -> list[int]:
    """select top k elements from nums using heap"""
    # initialize heap
    heap = []
    # push first k elements into heap  
    for i in range(k):
        heapq.heappush(heap, nums[i]) 
    # keep the size of heap to k, and replace the top element if necessary
    for i in range(k, len(nums)):
        # if the current element is larger than the top element of heap, replace it with the current element
        if nums[i] > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, nums[i])
    return heap


"""Driver Code"""
if __name__ == "__main__":
    nums = [1, 7, 6, 3, 2]
    k = 3

    res = top_k_heap(nums, k)
    print(f"top {k} elements of {nums} are")
    print_heap(res)