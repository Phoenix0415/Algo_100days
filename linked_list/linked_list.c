#include <stdlib.h>
#include <stdio.h>
#include "linked_list.h"

/* constructor of the linked list */
ListNode *newListNode(int val)
{
	ListNode *node;
	node = (ListNode *)malloc(sizeof(ListNode));
	node->val = val;
	node->next = NULL;
	return node;
}

/* insert node P after node n0 */
void insert(ListNode *n0, ListNode *P)
{
	ListNode *n1 = n0->next;
	P->next = n1;
	n0->next = P;
}

/* remove node P after node n0 */
// note: the keyword "remove" is used in stdio.h
void removeItem(ListNode *n0) 
{
    if (!n0->next)
        return;
    // n0 -> P -> n1
    ListNode *P = n0->next;
    ListNode *n1 = P->next;
    n0->next = n1;
    // release the memory of P
    free(P);
}

/* access the node at index */
ListNode *access(ListNode *head, int index)
{
	// traverse the linked list from head to index
    while (head && head->next && index)
	{
    	head = head->next;
    	index--;
    }
    return head;
}

/* search the node with target value */
int find(ListNode *head, int target)
{
    int index = 0;
    while (head)
	{
        if (head->val == target)
            return index;
        head = head->next;
        index++;
    }
    return -1;
}

/* traverse and print the linked list */
void traverse(ListNode *head)
{
    while (head)
    {
        printf("%d", head->val);
        if (head->next)
        {
            printf(" -> ");
        }
        head = head->next;
    }
    printf("\n");
}

int main()
{
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

	printf("traverse the linked list:\n");
	traverse(n0);
	printf("\n");
	
	printf("insert node P(6) after n1(3):\n");
	insert(n1, newListNode(6));
	traverse(n0);
	printf("\n");

	printf("remove node P(6) after n1(3):\n");
	removeItem(n1);
	traverse(n0);
	printf("\n");

	ListNode *node = access(n0, 3);
	printf("access the node(5) at index 3: %d\n", node->val);
	printf("\n");

	printf("find the node with value 5, and report its index: %d\n",find(n0, 5));
	return 0;
}	

