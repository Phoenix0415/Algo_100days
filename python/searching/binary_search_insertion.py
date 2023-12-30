def binary_search_insertion_simple(nums: list[int], target: int) -> int:
    """binary search insertion (no repeated elements)"""
    i, j = 0, len(nums) - 1  # initialize a double closed interval [0, n-1]
    while i <= j:
        m = (i + j) // 2  # calculate the middle index m
        if nums[m] < target:
            i = m + 1  # the target is in the interval [m+1, j]
        elif nums[m] > target:
            j = m - 1  # the target is in the interval [i, m-1]
        else:
            return m  # the target is found, return its index
    # the target is not found, return the insertion point i
    return i


def binary_search_insertion(nums: list[int], target: int) -> int:
    """binary search insertion (with repeated elements)"""
    i, j = 0, len(nums) - 1  # initialize a double closed interval [0, n-1]
    while i <= j:
        m = (i + j) // 2  # calculate the middle index m
        if nums[m] < target:
            i = m + 1  # the target is in the interval [m+1, j]
        elif nums[m] > target:
            j = m - 1  # the target is in the interval [i, m-1]
        else:
            j = m - 1  # the first occurrence of the target is in the interval [i, m-1]
    # the target is not found, return the insertion point i
    return i


"""Driver Code"""
if __name__ == "__main__":
    # a sorted array without repeated elements
    nums = [1, 3, 6, 8, 12, 15, 23, 26, 31, 35]
    print(f"\nthe array nums = {nums}")
    # find the insertion point of an element
    for target in [6, 9]:
        index = binary_search_insertion_simple(nums, target)
        print(f"the insertion point of {target} is {index}")

    # a sorted array with repeated elements
    nums = [1, 3, 6, 6, 6, 6, 6, 10, 12, 15]
    print(f"\nthe array nums = {nums}")
    # find the insertion point of an element
    for target in [2, 6, 20]:
        index = binary_search_insertion(nums, target)
        print(f"the insertion point of {target} is {index}")