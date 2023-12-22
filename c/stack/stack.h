#ifndef STACK_H
#define STACK_H

/* implement of array stack */
typedef struct {
    int *data;
    int size;
} ArrayStack;

/* implement of linked list stack */
typedef struct {
    ListNode *top; // pointer to the top node
    int size;      // size of the stack
} LinkedListStack;

#endif // STACK_H