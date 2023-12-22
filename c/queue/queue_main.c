#include "queue.h"
#include <stdio.h>

int main() {
    // test linkedlist queue1 and its functions
    LinkedListQueue *queue1 = newLinkedListQueue();
    printf("initialize a linkedlist queue1\r\n");
    printLinkedListQueue(queue1);
    printf("is queue1 empty? %s\r\n", empty(queue1) ? "true" : "false");
    printf("enqueue 1, 2, 3, 4, 5\r\n");
    push(queue1, 1);
    push(queue1, 2);
    push(queue1, 3);
    push(queue1, 4);
    push(queue1, 5);
    printLinkedListQueue(queue1);
    printf("size of queue1: %d\r\n", size(queue1));
    printf("the front value of queue1: %d\r\n", peek(queue1));

    printf("dequeue 3 times\r\n");
    pop(queue1);
    pop(queue1);
    pop(queue1);
    printLinkedListQueue(queue1);
    printf("size of queue1: %d\r\n", size(queue1));

    printf("enqueue 6, 7, 8, 9, 10\r\n");
    push(queue1, 6);
    push(queue1, 7);
    push(queue1, 8);
    push(queue1, 9);
    push(queue1, 10);
    printLinkedListQueue(queue1);
    printf("size of queue1: %d\r\n", size(queue1));

    printf("delete the queue1\r\n");
    delLinkedListQueue(queue1);
    printLinkedListQueue(queue1);

    // test array queue and its functions
    ArrayQueue *queue2 = newArrayQueue(5);
    printf("initialize an array queue2\r\n");
    printf("is queue2 empty? %s\r\n", empty(queue2) ? "true" : "false");
    printf("enqueue 1, 2, 3, 4, 5\r\n");
    push(queue2, 1);
    push(queue2, 2);
    push(queue2, 3);
    push(queue2, 4);
    push(queue2, 5);
    printf("size of queue2: %d\r\n", size(queue2));
    printf("capacity of queue2: %d\r\n", capacity(queue2));
    printf("the front value of queue2: %d\r\n", peek(queue2));

    printf("dequeue 3 times\r\n");
    pop(queue2);
    pop(queue2);
    pop(queue2);
    printf("size of queue2: %d\r\n", size(queue2));

    printf("enqueue 6, 7, 8, 9, 10\r\n");
    push(queue2, 6);
    push(queue2, 7);
    push(queue2, 8);
    push(queue2, 9);
    push(queue2, 10);
    printf("size of queue2: %d\r\n", size(queue2));
    printf("capacity of queue2: %d\r\n", capacity(queue2));

    printf("delete the queue2\r\n");
    delArrayQueue(queue2);
    printLinkedListQueue(queue2);

    return 0;
}