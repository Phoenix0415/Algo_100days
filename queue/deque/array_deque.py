class ArrayDeque:
	"""deque implemented with array"""

	def __init__(self, capacity: int):
		"""constructor"""
		self._nums: list[int] = [0] * capacity
		self._front: int = 0
		self._size: int = 0

	def capacity(self) -> int:
		"""get the capacity of the deque"""
		return len(self._nums)

	def size(self) -> int:
		"""get the length of the deque"""
		return self._size

	def is_empty(self) -> bool:
		"""check if the deque is empty"""
		return self._size == 0

	def index(self, i: int) -> int:
		"""get the index of the element in the array"""
		# use the modulo operator to calculate the index of the element
		# when i exceeds the head of the array, it returns to the tail
		# when i exceeds the tail of the array, it returns to the head
		return (i + self.capacity()) % self.capacity()

	def push_first(self, num: int):
		"""enqueue at the front"""	
		if self._size == self.capacity():
			print("double linked list deque is full")
			return
		# move the front pointer backward by one
		# use module operator，set the front pointer to the tail of the array
		self._front = self.index(self._front - 1)
		# add the new element to the front
		self._nums[self._front] = num
		self._size += 1

	def push_last(self, num: int):
		"""enqueue at the rear"""
		if self._size == self.capacity():
			print("deque is full")
			return
		# calculate the index of the rear element
		rear = self.index(self._front + self._size)
		# add the new element to the rear
		self._nums[rear] = num
		self._size += 1

	def pop_first(self) -> int:
		"""dequeue at the front"""
		num = self.peek_first()
		# move the front pointer forward by one
		self._front = self.index(self._front + 1)
		self._size -= 1
		return num

	def pop_last(self) -> int:
		"""dequeue at the rear"""
		num = self.peek_last()
		self._size -= 1
		return num

	def peek_first(self) -> int:
		"""get the element at the front"""
		if self.is_empty():
			raise IndexError("the deque is empty")
		return self._nums[self._front]

	def peek_last(self) -> int:
		"""get the element at the rear"""
		if self.is_empty():
			raise IndexError("the deque is empty")
		# calculate the index of the rear element
		last = self.index(self._front + self._size - 1)
		return self._nums[last]

	def to_array(self) -> list[int]:
		"""convert the deque to an array"""
		# only the elements in the deque are converted to an array
		res = []
		for i in range(self._size):
			res.append(self._nums[self.index(self._front + i)])
		return res