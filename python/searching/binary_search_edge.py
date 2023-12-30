import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from binary_search_insertion import binary_search_insertion


def binary_search_left_edge(nums: list[int], target: int) -> int:
    """binary search the left edge of target"""
    # equivalent to binary_search_insertion(nums, target)
    i = binary_search_insertion(nums, target)
    # if the target is not found, return -1
    if i == len(nums) or nums[i] != target:
        return -1
    # if the target is found, return index i
    return i

def binary_search_right_edge(nums: list[int], target: int) -> int:
    """binary search the right edge of target"""
    # transform the problem to binary_search_insertion(nums, target + 1)
    i = binary_search_insertion(nums, target + 1)
    # j is the index of the right edge of target, which is the index of the first occurrence that is greater than target
    j = i - 1
    # if the target is not found, return -1
    if j == -1 or nums[j] != target:
        return -1
    # the target is found, return index j
    return j


"""Driver Code"""
if __name__ == "__main__":
    # a sorted array with repeated elements
    nums = [1, 3, 6, 6, 6, 6, 6, 10, 12, 15]
    print(f"\nthe array nums = {nums}")

    # find the left and right edges of an element
    for target in [6, 7]:
        index = binary_search_left_edge(nums, target)
        print(f"the left edge of {target} is {index}")
        index = binary_search_right_edge(nums, target)
        print(f"the right edge of {target} is {index}")