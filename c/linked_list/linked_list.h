#ifndef LINKED_LIST_H
#define LINKED_LIST_H

/* structure of singly linked list */
typedef struct ListNode
{
	int val;                 // the value of current node
	struct ListNode *next;	 // the pointer point to the next node
} ListNode;

/* structure of doubly linked list */
typedef struct DoublyListNode {
    int val;               // the value of current node
    struct DoublyListNode *next; // the pointer point to the next node
    struct DoublyListNode *prev; // the pointer point to the previous node
} DoublyListNode;

#endif