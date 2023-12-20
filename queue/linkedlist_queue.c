/* constructor */
LinkedListQueue *newLinkedListQueue() {
	LinkedListQueue *queue = (LinkedListQueue *)malloc(sizeof(LinkedListQueue));
	queue->front = NULL;
	queue->rear = NULL;
	queue->queSize = 0;
	return queue;
}

/* destructor */
void delLinkedListQueue(LinkedListQueue *queue) {
	// free all nodes
	for (int i = 0; i < queue->queSize && queue->front != NULL; i++) {
		ListNode *tmp = queue->front;
		queue->front = queue->front->next;
		free(tmp);
	}
	// free queue
	free(queue);
}

/* get queue size */
int size(LinkedListQueue *queue) {
	return queue->queSize;
}

/* check if queue is empty */
bool empty(LinkedListQueue *queue) {
	return (size(queue) == 0);
}

/* enqueue */
void push(LinkedListQueue *queue, int num) {
	// append a new node to the end of queue
	ListNode *node = newListNode(num);
	// if queue is empty, set front and rear to the new node
	if (queue->front == NULL) {
		queue->front = node;
		queue->rear = node;
	}
	// if queue is not empty, append the new node to the end of queue
	else {
		queue->rear->next = node;
		queue->rear = node;
	}
	queue->queSize++;
}

/* get the front element */
int peek(LinkedListQueue *queue) {
	assert(size(queue) && queue->front);
	return queue->front->val;
}

/* dequeue */
int pop(LinkedListQueue *queue) {
	int num = peek(queue);
	ListNode *tmp = queue->front;
	queue->front = queue->front->next;
	free(tmp);
	queue->queSize--;
	return num;
}

/* print queue */
void printLinkedListQueue(LinkedListQueue *queue) {
	int *arr = malloc(sizeof(int) * queue->queSize);
	// copy queue to array
	int i;
	ListNode *node;
	for (i = 0, node = queue->front; i < queue->queSize; i++) {
		arr[i] = node->val;
		node = node->next;
	}
	printArray(arr, queue->queSize);
	free(arr);
}