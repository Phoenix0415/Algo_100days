import random

# initializition of arrays
arr: list[int] = [0] * 5  # [ 0, 0, 0, 0, 0 ]
nums: list[int] = [1, 3, 2, 5, 4]

print("arr:",arr)
print("nums:",nums)

def random_access(nums: list[int]) -> int:
	"""access an element randomly"""
	# get a random index number from range[0, len(nums)-1]
	random_index = random.randint(0, len(nums) - 1)
	# get and return the number at this random index
	random_num = nums[random_index]
	return random_num

def insert(nums: list[int], num: int, index: int):
	"""insert element `num` at `index`(last element will be droped, 
	because arrays are fix-lengthed)"""
	# move elements from index `index` to last one one position backward
	for i in range(len(nums)-1, index , -1):
		nums[i] = nums[i-1]			
	nums[index] = num

def remove(nums: list[int], index: int):
	"""delete the element at index `index`"""
	# move all the elements after `index` one position forward
	for i in range(index, len(nums) - 1):
		nums[i] = nums[i + 1]
	# Reduce the length of the list by 1
	nums.pop()

def traverse(nums: list[int]):
	"""traverse the array"""
	count = 0
	for i in range(len(nums)):
		count += nums[i]
	"""
	# traverse each element directly
	for num in nums:
		count += num
	# or traverse both elements and index
	for i, num in enumerate(nums):
		count += nums[i]
		count += num
	"""
	return count;

def find(nums: list[int], target: int) -> int:
	"""find the provided element in the array"""
	for i in range(len(nums)):
		if nums[i] == target:
			return i
	return -1

def main():
	print("a random number in nums: ", random_access(nums))
	
	insert(nums, 6, 1)
	print("insert 6 in nums at index 1:", nums)
	
	remove(nums, 1)
	print("delete the elememt at index 1:", nums)
	
	print("traverse the array and print the sum of all elements: ", traverse(nums))
	
	print("find 5 in the nums, the index is(-1 if hasn't been found): ", find(nums, 5))
if __name__  == "__main__":
	main()
