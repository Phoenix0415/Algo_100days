def binary_search(nums: list[int], target: int) -> int:
    """binary search (double closed interval)"""
    # initialize a double closed interval [0, n-1]
    i, j = 0, len(nums) - 1
    # keep searching while the interval is not empty (i <= j)
    while i <= j:
        # theoretically, in python, the number can be infinitely large, so we don't need to worry about overflow
        m = (i + j) // 2  # calculate the middle index m
        if nums[m] < target:
            i = m + 1  # the target is in the interval [m+1, j]
        elif nums[m] > target:
            j = m - 1  # the target is in the interval [i, m-1]
        else:
            return m  # the target is found, return its index
    return -1  # the target is not found, return -1


def binary_search_lcro(nums: list[int], target: int) -> int:
    """binary search (left closed right open interval)"""
    # initialize a left closed right open interval [0, n)
    i, j = 0, len(nums)
    # keep searching while the interval is not empty (i < j) 
    while i < j:
        m = (i + j) // 2  # calculate the middle index m
        if nums[m] < target:
            i = m + 1  # the target is in the interval [m+1, j)
        elif nums[m] > target:
            j = m  # the target is in the interval [i, m)
        else:
            return m  # the target is found, return its index
    return -1  # the target is not found, return -1


"""Driver Code"""
if __name__ == "__main__":
    target = 6
    nums = [1, 3, 6, 8, 12, 15, 23, 26, 31, 35]

    # binary search (double closed interval)
    index: int = binary_search(nums, target)
    print("the index of target element 6 is ", index)
          
    # binary search (left closed right open interval)
    index: int = binary_search_lcro(nums, target)
    print("the index of target element 6 is ", index)