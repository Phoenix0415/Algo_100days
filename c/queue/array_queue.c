/* constructor */
ArrayQueue *newArrayQueue(int capacity) {
	ArrayQueue *queue = (ArrayQueue *)malloc(sizeof(ArrayQueue));
	// initialize queue
	queue->queCapacity = capacity;
	queue->nums = (int *)malloc(sizeof(int) * queue->queCapacity);
	queue->front = queue->queSize = 0;
	return queue;
}

/* destructor */
void delArrayQueue(ArrayQueue *queue) {
	free(queue->nums);
	free(queue);
}

/* get the capacity of queue */
int capacity(ArrayQueue *queue) {
	return queue->queCapacity;
}

/* get the size of queue */
int size(ArrayQueue *queue) {
	return queue->queSize;
}

/* check if queue is empty */
bool empty(ArrayQueue *queue) {
	return queue->queSize == 0;
}

/* access the front element */
int peek(ArrayQueue *queue) {
	assert(size(queue) != 0);
	return queue->nums[queue->front];
}

/* enqueue */
void push(ArrayQueue *queue, int num) {
	if (size(queue) == capacity(queue)) {
		printf("the queue if full\r\n");
		return;
	}
	// caulculate the rear index, point to the next position of the last element
	// implement circular queue by using mod
	int rear = (queue->front + queue->queSize) % queue->queCapacity;
	// append rear on the end of queue
	queue->nums[rear] = num;
	queue->queSize++;
}

/* dequeue */
int pop(ArrayQueue *queue) {
	int num = peek(queue);
	// move front to the next position, if front is the last element, move to the first position
	queue->front = (queue->front + 1) % queue->queCapacity;
	queue->queSize--;
	return num;
}