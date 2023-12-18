class ListNode:
	"""class of linked list"""
	def __init__(self, val: int):
		self.val: int = val					# the value of current node
		self.next: ListNode | None = None 	# the refenrence of the next node

# initialize the linked list: 1 -> 3 -> 2 -> 5 -> 4
# step1: initialize all the nodes
n0 = ListNode(1)
n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(5)
n4 = ListNode(4)

# step2: link all the nodes
n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4


