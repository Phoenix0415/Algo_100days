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

print("a random number in nums: ",random_access(nums))
