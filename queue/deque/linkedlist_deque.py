class ListNode:
	"""doble linked list node"""

	def __init__(self, val: int):
		"""constructor"""
		self.val: int = val
		self.next: ListNode | None = None  # successor node reference
		self.prev: ListNode | None = None  # prodecessor node reference

class LinkedListDeque:
	"""deque implemented by double linked list"""

	def __init__(self):
		"""constructor"""
		self._front: ListNode | None = None  # front node
		self._rear: ListNode | None = None  # rear node
		self._size: int = 0  # length of the deque

	def size(self) -> int:
		"""get the length of the deque"""
		return self._size

	def is_empty(self) -> bool:
		"""check if the deque is empty"""
		return self.size() == 0

	def push(self, num: int, is_front: bool):
		"""enqueue operation"""
		node = ListNode(num)
		# if the deque is empty, set the front and rear node to the new node
		if self.is_empty():
			self._front = self._rear = node
		# enqueue at the front
		elif is_front:
			# add the new node to the front
			self._front.prev = node
			node.next = self._front
			self._front = node  # update the front node
		# enqueue at the rear
		else:
			# add the new node to the rear 
			self._rear.next = node
			node.prev = self._rear
			self._rear = node  # update the rear node
		self._size += 1  # update the length of the deque

	def push_first(self, num: int):
		"""enqueue at the front"""
		self.push(num, True)

	def push_last(self, num: int):
		"""enqueue at the rear"""
		self.push(num, False)

	def pop(self, is_front: bool) -> int:
		"""dequeue operation"""
		if self.is_empty():
			raise IndexError("double linked list deque is empty")
		# dequeue at the front
		if is_front:
			val: int = self._front.val  # store the value of the front node temporarily
			# delete the front node
			fnext: ListNode | None = self._front.next
			if fnext != None:
				fnext.prev = None
				self._front.next = None
			self._front = fnext  # update the front node
		# dequeue at the rear
		else:
			val: int = self._rear.val  # store the value of the rear node temporarily
			# delete the rear node
			rprev: ListNode | None = self._rear.prev
			if rprev != None:
				rprev.next = None
				self._rear.prev = None
			self._rear = rprev  # update the rear node
		self._size -= 1  # update the length of the deque
		return val

	def pop_first(self) -> int:
		"""enqueue at the front"""
		return self.pop(True)

	def pop_last(self) -> int:
		"""dequeue at the rear"""
		return self.pop(False)

	def peek_first(self) -> int:
		"""get the value of the front node"""
		if self.is_empty():
			raise IndexError("the deque is empty")
		return self._front.val

	def peek_last(self) -> int:
		"""get the value of the rear node"""
		if self.is_empty():
			raise IndexError("the deque is empty")
		return self._rear.val

	def to_array(self) -> list[int]:
		"""convert the deque to an array"""
		node = self._front
		res = [0] * self.size()
		for i in range(self.size()):
			res[i] = node.val
			node = node.next
		return res