from linkedlist_deque import LinkedListDeque
from array_deque import ArrayDeque

# test of two versions of deque implementation
def main():
    """ initialize deque1 with array, and do some operations """
    deque1 = ArrayDeque(3)
    print("Initialize deque1 with array. Whether it is empty:",deque1.is_empty())
    print("")
    
    deque1.push_first(1)
    deque1.push_first(2)
    print("push 1,2 using push_first to the deque1:", deque1.to_array())
    deque1.push_last(3)
    print("push 3 using push_last to the deque1:", deque1.to_array())
    print("")
    
    print("the front element of the deque1 is:", deque1.peek_first())
    print("the rear element of the deque1 is:", deque1.peek_last())
    print("")
    
    print("the size of the deque1 is:", deque1.size())
    print("the capacity of the deque1 is:", deque1.capacity())
    print("")
    
    print("the index of the front element of the deque1 is:", deque1.index(deque1._front))
    deque1.pop_first()
    print("pop the front element of the deque1:", deque1.to_array())
    deque1.pop_last()
    print("pop the rear element of the deque1:", deque1.to_array())
    print("-------------------------------------------------------")

    """ initialize deque2 with linked list, and do some operations """
    deque2 = LinkedListDeque()
    print("Initialize deque2 with linked list. Whether it is empty:",deque2.is_empty())
    print("")
    
    deque2.push_first(1)
    deque2.push_first(2)
    print("push 1,2 to the deque2 using push_first:", deque2.to_array())
    deque2.push_last(3)
    print("push 3 to the deque2 using push_last:", deque2.to_array())
    deque2.push(4,True)
    print("push 4 to the deque2 using push:", deque2.to_array())
    deque2.push(5,False)
    print("push 5 to the deque2 using push:", deque2.to_array())
    print("")
    
    print("the front element of the deque2 is:", deque2.peek_first())
    print("the rear element of the deque2 is:", deque2.peek_last())
    print("")
    
    print("the size of the deque2 is:", deque2.size())
    print("")

    deque2.pop_first()
    print("pop the front element of the deque2 using pop_first:", deque2.to_array())
    deque2.pop_last()
    print("pop the rear element of the deque2 using pop_last:", deque2.to_array())
    deque2.pop(True)
    print("pop the front element of the deque2 using pop:", deque2.to_array())
    deque2.pop(False)
    print("pop the rear element of the deque2 using pop:", deque2.to_array())
    
if __name__ == "__main__":
    main()
