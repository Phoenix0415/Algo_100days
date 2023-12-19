from linkedlist_stack import LinkedListStack
from array_stack import ArrayStack

def main():
	""" initialize stack1 with array, and do some operations """
	stack1 = ArrayStack()
	print("initialize stack1. whether it is empty:",stack1.is_empty())

	stack1.push(1)
	stack1.push(2)
	stack1.push(3)
	print("push 1,2,3 to the stack1:", stack1.to_list())
	print("the top element of the stack1 is:", stack1.peek())
	print("the size of the stack1 is:", stack1.size())

	stack1.pop()
	print("pop the top element of the stack1:", stack1.to_list())

	""" initialize stack2 with linked list, and do some operations """
	stack2 = LinkedListStack()
	print("initialize stack2. whether it is empty:",stack2.is_empty())

	stack2.push(1)
	stack2.push(2)
	stack2.push(3)
	print("push 1,2,3 to the stack2:", stack2.to_list())
	print("the top element of the stack2 is:", stack2.peek())
	print("the size of the stack2 is:", stack2.size())

	stack2.pop()
	print("pop the top element of the stack2:", stack2.to_list())
	
if __name__ == "__main__":
    main()
