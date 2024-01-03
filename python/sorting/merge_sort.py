def merge(nums: list[int], left: int, mid: int, right: int):
    """Merge the left and right subarrays"""
    # Create a temporary array 'tmp' to store the merged result
    tmp = [0] * (right - left + 1)
    # Initialize indices for the left and right subarrays and the temporary array
    i, j, k = left, mid + 1, 0
    
    # Compare elements from both subarrays and copy the smaller element to 'tmp'
    while i <= mid and j <= right: # when both subarrays have elements
        if nums[i] <= nums[j]: # when the left subarray has smaller element
            tmp[k] = nums[i] # copy the smaller element to 'tmp'
            i += 1 # move the index of left subarray to the next element
        else: # when the right subarray has smaller element
            tmp[k] = nums[j] # copy the smaller element to 'tmp'
            j += 1 # move the index of right subarray to the next element
        k += 1 # move the index of 'tmp' to the next element
        
    # Copy any remaining elements from both subarrays to 'tmp'
    while i <= mid: # when the left subarray has remaining elements
        tmp[k] = nums[i] # copy the remaining elements to 'tmp'
        i += 1 # move the index of left subarray to the next element
        k += 1 # move the index of 'tmp' to the next element
    while j <= right: # when the right subarray has remaining elements
        tmp[k] = nums[j] # copy the remaining elements to 'tmp'
        j += 1 # move the index of right subarray to the next element
        k += 1 # move the index of 'tmp' to the next element
        
    # Copy elements from 'tmp' back to the original array 'nums'
    for k in range(0, len(tmp)): # iterate through the temporary array
        nums[left + k] = tmp[k] # copy the element to the original array

def merge_sort(nums: list[int], left: int, right: int):
    """Merge sort"""
    # Base case: When the subarray has only one element, return
    if left >= right:
        return
    # Divide phase: Calculate the middle point
    mid = (left + right) // 2
    # Recursive calls to sort the left and right subarrays
    merge_sort(nums, left, mid)
    merge_sort(nums, mid + 1, right)
    # Merge phase: Merge the sorted left and right subarrays
    merge(nums, left, mid, right)


"""Driver Code"""
if __name__ == "__main__":
    nums = [7, 3, 2, 6, 0, 1, 5, 4]
    merge_sort(nums, 0, len(nums) - 1)
    print("after merge sort, nums =", nums)