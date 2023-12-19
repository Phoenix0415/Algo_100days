class MyList:
    """class of list"""

    def __init__(self):
        """constructor method"""
        self._capacity: int = 10  # capacity of the list
        self._arr: list[int] = [0] * self._capacity  # array (store elements of list)
        self._size: int = 0  # length of list（current number of list）
        self._extend_ratio: int = 2  # The multiple of each list expansion

    def size(self) -> int:
        """get the length of list"""
        return self._size

    def capacity(self) -> int:
        """get the capacity of list"""
        return self._capacity

    def get(self, index: int) -> int:
        """access element at index"""
        # index out of range
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")
        return self._arr[index]

    def set(self, num: int, index: int):
        """update element at index"""
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")
        self._arr[index] = num

    def add(self, num: int):
        """append element at the end"""
        # the number of elements exceeds the capacity, trigger the expansion mechanism
        if self.size() == self.capacity():
            self.extend_capacity()
        self._arr[self._size] = num
        self._size += 1

    def insert(self, num: int, index: int):
        """insert element at index"""
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")
        # the number of elements exceeds the capacity, trigger the expansion mechanism
        if self._size == self.capacity():
            self.extend_capacity()
        # move the elements after the index one position backwards
        for j in range(self._size - 1, index - 1, -1):
            self._arr[j + 1] = self._arr[j]
        self._arr[index] = num
        # update the number of elements
        self._size += 1

    def remove(self, index: int) -> int:
        """delete element at index"""
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")
        num = self._arr[index]
        # move the elements after the index one position forwards
        for j in range(index, self._size - 1):
            self._arr[j] = self._arr[j + 1]
        # update the number of elements
        self._size -= 1
        # return the deleted element
        return num

    def extend_capacity(self):
        """expand the capacity of list"""
        # create a new list with a larger capacity, and copy the elements of the original list to the new list
        self._arr = self._arr + [0] * self.capacity() * (self._extend_ratio - 1)
        # update the capacity
        self._capacity = len(self._arr)

    def to_array(self) -> list[int]:
        """convert list to array"""
        return self._arr[: self._size]

def main():
	# initialize a list
	# without initial values
	nums1: list[int] = []
	# with initial values
	nums: list[int] = [1, 3, 2, 5, 4]
	print("nums1:", nums1)
	print("nums:", nums)
	
	# access element
	num: int = nums[1]
	print("acess element at index 1:", num)

	# update element
	nums[1] = 0  # update value at index 1 to 0
	print("update value at index 1 to 0:", nums)
	
	# clear the list
	nums.clear()
	print("clear the list:", nums)
	
	# append elements at the end
	nums.append(6)
	print("append element 6 at the end:", nums)
	nums.append(7)
	print("append element 7 at the end:", nums)

	# insert element in the middle
	nums.insert(1, 0)   # insert 6 at index 1
	print("insert 0 at index 1:", nums)
	
	# delete element
	nums.pop(1)  #delete element at index 1
	print("delete element(0) at index 1:", nums)
	
	# traverse the list using index
	print("the list nums:", nums)
	count1 = 0
	for i in range(len(nums)):
		count1 += nums[i]
	print("traverse the list using index, report the sum of elements:", count1)
	
	count2 = 0
	# traverse the list directly
	for num in nums:
		count2 += num
	print("traverse the list directly, report the sum of elements:", count2)
	
	# concatenate two lists
	nums1: list[int] = [6, 8,7, 10 ,9]
	nums += nums1
	print("concatenate another list at the end of original one:", nums)
	
	# sort
	nums.sort() # default in ascending order
	print("sorting the list:", nums)	
	
if __name__ == "__main__":
	main()
