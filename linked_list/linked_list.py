class ListNode:
	"""singly linked list"""
	def __init__(self, val: int):
		self.val: int = val					# the value of current node
		self.next: ListNode | None = None 	# pointer point to next node

class ListNode:
    """doubly linked list"""
    def __init__(self, val: int):
        self.val: int = val                # value of current node
        self.next: ListNode | None = None  # pointer point to sucessor
        self.prev: ListNode | None = None  # pointer point to predecessor

def insert(n0: ListNode, P: ListNode):
	"""insert node P after node n0"""
	n1 = n0.next
	P.next = n1
	n0.next = P

def remove(n0: ListNode):
    """delete the first node after node n0"""
    if not n0.next:
        return
    # n0 -> P -> n1
    P = n0.next
    n1 = P.next
    n0.next = n1

def access(head: ListNode, index: int) -> ListNode | None:
    """visit the node at index `index`"""
    for _ in range(index):
        if not head:
            return None
        head = head.next
    return head

def find(head: ListNode, target: int) -> int:
    """find the first node has value `target`"""
    index = 0
    while head:
        if head.val == target:
            return index
        head = head.next
        index += 1
    return -1

def traverse(head: ListNode):
	"""traverse all the nodes and print them"""
	current_node = head
	linked_list_str = ""

	while current_node != None:
		# Append the value of the current node to the string
		linked_list_str += str(current_node.val)
		# Move to the next node
		current_node = current_node.next

		# Add '->' if there's another node
		if current_node != None:
			linked_list_str += " -> "

	# Print the formatted linked list string
	print( linked_list_str)

def main():
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
	
	print("traverse the singly linked list: ")
	traverse(n0)
	print("")

	P = ListNode(6)
	insert(n1,P)
	print("insert node(6) after n1(3):")
	traverse(n0)		
	print("")

	remove(n1)
	print("remove P(6):")
	traverse(n0)
	print("")

	value_ind3 = access(n0,3)
	print("access node at index 3: ",value_ind3.val)
	print("")	
	
	print("find node with value at 5, the index is: ",find(n0, 5))
	print("")

if __name__ == "__main__":
	main()
