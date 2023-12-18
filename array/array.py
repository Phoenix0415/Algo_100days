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

print("a random number in nums: ", random_access(nums))
insert(nums, 6, 1)
print("insert 6 in nums at index 1:", nums)
remove(nums, 1)
print("delete the elememt at index 1:", nums)
