#ifndef QUEUE_H
#define QUEUE_H

/* implement of linkedlist queue */
typedef struct {
	ListNode *front, *rear;
	int queSize;
} LinkedListQueue;

/* implement of array queue */
typedef struct {
	int *nums;       // array of queue
	int front;       // front pointer
	int queSize;     // rear pointer, point to the next position of the last element
	int queCapacity; // capacity of queue
} ArrayQueue;

LinkedListQueue *newLinkedListQueue(); // create a new queue
void delLinkedListQueue(LinkedListQueue *queue); // delete a queue
int size(LinkedListQueue *queue); // get the size of queue
bool empty(LinkedListQueue *queue); // check if the queue is empty
void push(LinkedListQueue *queue, int val); // push a value into queue
int peek(LinkedListQueue *queue); // get the front value of queue
int pop(LinkedListQueue *queue); // pop the front value of queue
void printLinkedListQueue(LinkedListQueue *queue); // print the queue

ArrayQueue *newArrayQueue(int capacity); // create a new queue
void delArrayQueue(ArrayQueue *queue); // delete a queue
int capacity(ArrayQueue *queue); // get the capacity of queue
int size(ArrayQueue *queue); // get the size of queue
bool empty(ArrayQueue *queue); // check if the queue is empty
bool peek(ArrayQueue *queue, int *val); // get the front value of queue
bool push(ArrayQueue *queue, int val); // push a value into queue
bool pop(ArrayQueue *queue, int *val); // pop the front value of queue

#endif