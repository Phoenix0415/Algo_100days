/*  implement stack with linked list */
LinkedListStack *newLinkedListStack() {
    LinkedListStack *s = malloc(sizeof(LinkedListStack));
    s->top = NULL;
    s->size = 0;
    return s;
}

/* destructor */
void delLinkedListStack(LinkedListStack *s) {
    while (s->top) {
        ListNode *n = s->top->next;
        free(s->top);
        s->top = n;
    }
    free(s);
}

/* get the size of stack */
int size(LinkedListStack *s) {
    assert(s);
    return s->size;
}

/* check if the stack is empty */
bool isEmpty(LinkedListStack *s) {
    assert(s);
    return size(s) == 0;
}

/* get the top element of stack */
int peek(LinkedListStack *s) {
    assert(s);
    assert(size(s) != 0);
    return s->top->val;
}

/* push element into stack */
void push(LinkedListStack *s, int num) {
    assert(s);
    ListNode *node = (ListNode *)malloc(sizeof(ListNode));
    node->next = s->top; // update next pointer
    node->val = num;     // update value
    s->top = node;       // update top pointer
    s->size++;           // update size
}

/* pop element out of stack */
int pop(LinkedListStack *s) {
    if (s->size == 0) {
        printf("stack is empty.\n");
        return INT_MAX;
    }
    assert(s);
    int val = peek(s);
    ListNode *tmp = s->top;
    s->top = s->top->next;
    // free memory
    free(tmp);
    s->size--;
    return val;
}
