from linkedlist_stack import LinkedListStack
from array_stack import ArrayStack

def main():
    """ initialize stack with array, and do some operations """
    stack = ArrayStack()
    print("initialize a stack, is it empty:",stack.is_empty())
    
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("push 1,2,3 to the stack:", stack.to_list())
    print("the top element of the stack is:", stack.peek())
    print("the size of the stack is:", stack.size())
    
    stack.pop()
    print("pop the top element of the stack:", stack.to_list())
    
if __name__ == "__main__":
    main()