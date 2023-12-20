from collections import deque

# initialize a deque
deque: deque[int] = deque()

# enqueue
deque.append(2)      # add to the rear
deque.append(5)
deque.append(4)
deque.appendleft(3)  # add to the front
deque.appendleft(1)

# get the element at the front and rear
front: int = deque[0]  # front element
rear: int = deque[-1]  # rear element

# dequeue
pop_front: int = deque.popleft()  # element at the front is dequeued
pop_rear: int = deque.pop()       # element at the rear is dequeued

# get the size of the deque
size: int = len(deque)

# check if the deque is empty
is_empty: bool = len(deque) == 0