
from linked_list import ListNode, insert, remove, access, find, traverse

class LinkedListQueue:
	"""implement queue with linked list"""

	def __init__(self):
		"""constructor"""
		self._front: ListNode | None = None  # front node
		self._rear: ListNode | None = None  # rear node
		self._size: int = 0

	def size(self) -> int:
		"""get the length"""
		return self._size

	def is_empty(self) -> bool:
		"""check if it is empty"""
		return not self._front

	def push(self, num: int):
		"""enqueue"""
		# append element after rear node num
		node = ListNode(num)
		# if the queue is empty, both front and rear nodes point to the appended node
		if self._front is None:
			self._front = node
			self._rear = node
		# if the queue is not empty, the rear node point to the appended node
		else:
			self._rear.next = node
			self._rear = node
		self._size += 1

	def pop(self) -> int:
		"""dequeue"""
		num = self.peek()
		# delete front node
		self._front = self._front.next
		self._size -= 1
		return num
	
	def peek(self) -> int:
		"""get the front node"""
		if self.is_empty():
			raise IndexError("the queue is empty")
		return self._front.val

	def to_list(self) -> list[int]:
		"""convert queue to list"""
		queue = []
		temp = self._front
		while temp:
			queue.append(temp.val)
			temp = temp.next
		return queue
