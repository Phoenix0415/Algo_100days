def selection_sort(nums: list[int]):
    """selection_sort"""
    n = len(nums)
    # outer loop: sort the unsorted part, which is [i, n-1], i = 0, 1, ..., n-2
    for i in range(n - 1):
        # inner loop: find the minimum element in the unsorted part
        k = i # k is the index of the minimum element
        for j in range(i + 1, n):
            if nums[j] < nums[k]:
                k = j  # update the index of the minimum element
        # swap the minimum element with the first element(which is nums[i]) of the unsorted part
        nums[i], nums[k] = nums[k], nums[i]


"""Driver Code"""
if __name__ == "__main__":
    nums = [4, 1, 3, 1, 5, 2]
    selection_sort(nums)
    print("Sorted nums: ", nums)