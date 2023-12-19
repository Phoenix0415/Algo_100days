# initialize a stack
# there are no built-in stack in python, so we use list to implement stack
stack: list[int] = []
print("initialize a stack:",stack)

# put elements to the stack
stack.append(1)
stack.append(3)
stack.append(2)
stack.append(5)
stack.append(4)
print("put 1,3,2,5,4 to the stack:",stack)

# get the top element
peek: int = stack[-1]
print("get the top element:",peek)

# pop the top element
pop: int = stack.pop()
print("pop the top element:",pop)
print("stack after pop the top element:",stack)

# get the size of the stack
size: int = len(stack)
print("get the size of the stack:",size)

# check if the stack is empty
is_empty: bool = len(stack) == 0
print("check if the stack is empty:",is_empty)