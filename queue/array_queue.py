class ArrayQueue:
	"""implement queue with circular array"""

	def __init__(self, size: int):
		"""constructor"""
		self._nums: list[int] = [0] * size  # array to store elements
		self._front: int = 0  # pointer to front of queue
		self._size: int = 0  # size of queue

	def capacity(self) -> int:
		"""get capacity of queue"""
		return len(self._nums)

	def size(self) -> int:
		"""get size of queue"""
		return self._size

	def is_empty(self) -> bool:
		"""check if queue is empty"""
		return self._size == 0

	def push(self, num: int):
		"""enqueue"""
		if self._size == self.capacity():
			raise IndexError("the queue is full")
		# calculate rear pointer, point to the next position of the last element
		# use mod to make sure the rear pointer can skip the end of array and point back to the start of array
		rear: int = (self._front + self._size) % self.capacity()
		# add element to the rear of queue
		self._nums[rear] = num
		self._size += 1

	def pop(self) -> int:
		"""dequeue"""
		num: int = self.peek()
		# move front pointer to the next position of the first element
		self._front = (self._front + 1) % self.capacity()
		self._size -= 1
		return num

	def peek(self) -> int:
		"""get the first element of queue"""
		if self.is_empty():
			raise IndexError("the queue is empty")
		return self._nums[self._front]

	def to_list(self) -> list[int]:
		"""convert queue to list"""
		res = [0] * self.size()
		j: int = self._front
		for i in range(self.size()):
			res[i] = self._nums[(j % self.capacity())]
			j += 1
		return res