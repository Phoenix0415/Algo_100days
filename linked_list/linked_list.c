#include <stdlib.h>

/* structure of linked list */
typedef struct ListNode
{
	int val;                 // the value of current node
	struct ListNode *next;	 // the pointer point to the next node
} ListNode;

/* constructor of the linked list */
ListNode *newListNode(int val)
{
	ListNode *node;
	node = (ListNode *)malloc(sizeof(ListNode));
	node->val = val;
	node->next = NULL;
	return node;
}


/* initialize the linked list: 1 -> 3 -> 2 -> 5 -> 4 */
// step1: initialize all the nodes
ListNode *n0 = newListNode(1);
ListNode *n1 = newListNode(3);
ListNode *n2 = newListNode(2);
ListNode *n3 = newListNode(5);
ListNode *n4 = newListNode(4);

// step2: link all the node
n0->next = n1;
n1->next = n2;
n2->next = n3;
n3->next = n4;

/* insert node P after node n0 */
void insert(ListNode *n0, ListNode *P)
{
	P->next = n1;
	n0->next = P;
}


