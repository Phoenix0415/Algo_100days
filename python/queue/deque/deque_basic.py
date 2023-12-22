from collections import deque

# initialize a deque
deque: int = deque()
print("initialize a deque:",deque)  # deque([])

# enqueue
deque.append(2)      # add to the rear
deque.append(5)
deque.append(4)
print("enqueue 2, 5, 4:",deque)  # deque([2, 5, 4])
deque.appendleft(3)  # add to the front
deque.appendleft(1)
print("enqueue on the left 3, 1:",deque)  # deque([1, 3, 2, 5, 4])

# get the element at the front and rear
front: int = deque[0]  # front element
print("front:",front)  # front: 1
rear: int = deque[-1]  # rear element
print("rear:",rear)    # rear: 4

# dequeue
pop_front: int = deque.popleft()  # element at the front is dequeued
print("dequeued front using popleft:",deque)  # deque([3, 2, 5, 4]
pop_rear: int = deque.pop()       # element at the rear is dequeued
print("dequeue using pop:",deque)  # deque([3, 2, 5])

# get the size of the deque
size: int = len(deque)
print("size of the deque:",size)  # size of the deque: 3

# check if the deque is empty
is_empty: bool = len(deque) == 0
print("is the deque empty:",is_empty)  # is the deque empty: False