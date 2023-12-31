def insertion_sort(nums: list[int]):
    """insertion sort"""
    # outer loop: the sorted part is [0, i-1]
    # the left part of base is sorted, the right part is unsorted
    for i in range(1, len(nums)): # i is the index of base, i.e., the element to be inserted
        base = nums[i]
        j = i - 1
        # inner loop: find the correct position to insert base
        while j >= 0 and nums[j] > base:
            nums[j + 1] = nums[j]  # move nums[j] to the right by 1
            j -= 1
        nums[j + 1] = base  # insert base into the correct position


"""Driver Code"""
if __name__ == "__main__":
    nums = [4, 1, 3, 1, 5, 2]
    insertion_sort(nums)
    print("after insertion sort: ", nums)