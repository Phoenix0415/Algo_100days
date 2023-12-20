from linkedlist_queue import LinkedListQueue
from array_queue import ArrayQueue

def main():
    """ initialize queue1 with array, and do some operations """
    queue1 = ArrayQueue(3)
    print("Initialize queue1 with array. Whether it is empty:",queue1.is_empty())

    queue1.push(1)
    queue1.push(2)
    queue1.push(3)
    print("push 1,2,3 to the queue1:", queue1.to_list())
    print("the front element of the queue1 is:", queue1.peek())
    print("the size of the queue1 is:", queue1.size())

    queue1.pop()
    print("pop the front element of the queue1:", queue1.to_list())
    print("")
    
    """ initialize queue2 with linked list, and do some operations """
    queue2 = LinkedListQueue()
    print("Initialize queue2 with linked list. Whether it is empty:",queue2.is_empty())

    queue2.push(1)
    queue2.push(2)
    queue2.push(3)
    print("push 1,2,3 to the queue2:", queue2.to_list())
    print("the front element of the queue2 is:", queue2.peek())
    print("the size of the queue2 is:", queue2.size())

    queue2.pop()
    print("pop the front element of the queue2:", queue2.to_list())

if __name__ == "__main__":
    main()