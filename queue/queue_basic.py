from collections import deque

# initialize a queue
# in python, we use deque to implement queue
# though we can use queue.Queue, but it is not recommended because it's not very handy
que: deque[int] = deque()
print("initialize a queue:",que)
# append elements to the queue
que.append(1)
que.append(3)
que.append(2)
que.append(5)
que.append(4)
print("append 1,3,2,5,4. queue:",que)

# get the front element
front: int = que[0];
print("get the front element:",front)

# pop the front element
pop: int = que.popleft()
print("pop the front element:",pop)
print("queue:",que)

# get the size of the queue
size: int = len(que)
print("get the size of the queue:",size)

# check if the queue is empty
is_empty: bool = len(que) == 0
print("check if the queue is empty:",is_empty)