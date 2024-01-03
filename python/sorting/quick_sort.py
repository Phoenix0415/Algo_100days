class QuickSort:
    """quick sort class"""

    def partition(self, nums: list[int], left: int, right: int) -> int:
        """pivot partition"""
        # use nums[left] as pivot
        i, j = left, right
        while i < j:
            while i < j and nums[j] >= nums[left]:
                j -= 1  # find the first element less than pivot from right to left 
            while i < j and nums[i] <= nums[left]:
                i += 1  # find the first element greater than pivot from left to right
            # swap elements
            nums[i], nums[j] = nums[j], nums[i]
        # swap pivot to the boundary of two subarrays
        nums[i], nums[left] = nums[left], nums[i]
        return i  # return the index of pivot

    def quick_sort(self, nums: list[int], left: int, right: int):
        """quick sort"""
        # stop recursion when the length of subarray is 1
        if left >= right:
            return
        # pivot partition
        pivot = self.partition(nums, left, right)
        # recursion on left subarray and right subarray
        self.quick_sort(nums, left, pivot - 1)
        self.quick_sort(nums, pivot + 1, right)


class QuickSortMedian:
    """quick sort class (median pivot optimization)"""

    def median_three(self, nums: list[int], left: int, mid: int, right: int) -> int:
        """choose the median of three numbers as pivot"""
        # use xor rule: 0 ^ 0 = 1 ^ 1 = 0, 0 ^ 1 = 1 ^ 0 = 1 ro simplify the if condition
        if (nums[left] < nums[mid]) ^ (nums[left] < nums[right]):
            return left
        elif (nums[mid] < nums[left]) ^ (nums[mid] < nums[right]):
            return mid
        return right

    def partition(self, nums: list[int], left: int, right: int) -> int:
        """pivot partition(choose the median of three numbers as pivot)"""
        # choose nums[left] as pivot
        med = self.median_three(nums, left, (left + right) // 2, right)
        # swap pivot to the left boundary of subarray
        nums[left], nums[med] = nums[med], nums[left]
        # choose nums[left] as pivot
        i, j = left, right
        while i < j:
            while i < j and nums[j] >= nums[left]:
                j -= 1  # find the first element less than pivot from right to left
            while i < j and nums[i] <= nums[left]:
                i += 1  # find the first element greater than pivot from left to right
            # 元素交换
            nums[i], nums[j] = nums[j], nums[i]
        # swap pivot to the boundary of two subarrays   
        nums[i], nums[left] = nums[left], nums[i]
        return i  # return the index of pivot

    def quick_sort(self, nums: list[int], left: int, right: int):
        """quick sort (median pivot optimization)"""
        # stop recursion when the length of subarray is 1
        if left >= right:
            return
        # pivot partition
        pivot = self.partition(nums, left, right)
        # recursion on left subarray and right subarray
        self.quick_sort(nums, left, pivot - 1)
        self.quick_sort(nums, pivot + 1, right)


class QuickSortTailCall:
    """quick sort class (tail call optimization)"""

    def partition(self, nums: list[int], left: int, right: int) -> int:
        """pivot partition"""
        # use nums[left] as pivot
        i, j = left, right
        while i < j:
            while i < j and nums[j] >= nums[left]:
                j -= 1  # find the first element less than pivot from right to left
            while i < j and nums[i] <= nums[left]:
                i += 1  # find the first element greater than pivot from left to right
            # swap elements
            nums[i], nums[j] = nums[j], nums[i]
        # swap pivot to the boundary of two subarrays
        nums[i], nums[left] = nums[left], nums[i]
        return i  # return the index of pivot

    def quick_sort(self, nums: list[int], left: int, right: int):
        """quick sort (tail call optimization)"""
        # stop recursion when the length of subarray is 1
        while left < right:
            # pivot partition
            pivot = self.partition(nums, left, right)
            # recursion on the shorter subarray
            if pivot - left < right - pivot:
                self.quick_sort(nums, left, pivot - 1)  # recursion on left subarray
                left = pivot + 1  # remaining unsorted subarray is [pivot + 1, right]
            else:
                self.quick_sort(nums, pivot + 1, right)  # recursion on right subarray
                right = pivot - 1  # remaining unsorted subarray is [left, pivot - 1]


"""Driver Code"""
if __name__ == "__main__":
    # quick sort
    nums = [2, 4, 1, 0, 3, 5]
    QuickSort().quick_sort(nums, 0, len(nums) - 1)
    print("after quick sort, nums =", nums)

    # quick sort (median pivot optimization)
    nums1 = [2, 4, 1, 0, 3, 5]
    QuickSortMedian().quick_sort(nums1, 0, len(nums1) - 1)
    print("after quick sort (median pivot optimization), nums =", nums1)

    # quick sort (tail call optimization)
    nums2 = [2, 4, 1, 0, 3, 5]
    QuickSortTailCall().quick_sort(nums2, 0, len(nums2) - 1)
    print("after quick sort (tail call optimization), nums =", nums2)