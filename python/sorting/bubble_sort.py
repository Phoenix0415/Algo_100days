def bubble_sort(nums: list[int]):
    """bubble sort"""
    n = len(nums)
    # outer loop: sort the unsorted part, which is [0, i], i = n-1, n-2, ..., 1
    for i in range(n - 1, 0, -1): # i is the right boundary of the unsorted part
        # inner loop: bubble the maximum element in the unsorted part to the right
        for j in range(i):
            if nums[j] > nums[j + 1]:
                # swap nums[j] and nums[j + 1]
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


def bubble_sort_with_flag(nums: list[int]):
    """bubble sort with flag"""
    n = len(nums)
    # outer loop: sort the unsorted part, which is [0, i], i = n-1, n-2, ..., 1
    for i in range(n - 1, 0, -1):
        flag = False  # init flag
        # inner loop: bubble the maximum element in the unsorted part to the right
        for j in range(i):
            if nums[j] > nums[j + 1]:
                # swap nums[j] and nums[j + 1]
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = True  # reset flag
        if not flag:
            break  # no swap in this round, so the array is already sorted


"""Driver Code"""
if __name__ == "__main__":
    nums = [4, 1, 3, 1, 5, 2]
    bubble_sort(nums)
    print("after bubble sort, nums =", nums)

    nums1 = [4, 1, 3, 1, 5, 2]
    bubble_sort_with_flag(nums1)
    print("after bubble sort with flag, nums1 =", nums1)