/* constructor */
ArrayStack *newArrayStack() {
    ArrayStack *stack = malloc(sizeof(ArrayStack));
    // initialize enough memory to avoid segmentation fault
    stack->data = malloc(sizeof(int) * MAX_SIZE);
    stack->size = 0;
    return stack;
}

/* destructor */
void delArrayStack(ArrayStack *stack) {
    free(stack->data);
    free(stack);
}

/* get size of stack */
int size(ArrayStack *stack) {
    return stack->size;
}

/* check if stack is empty */
bool isEmpty(ArrayStack *stack) {
    return stack->size == 0;
}

/* push element into stack */
void push(ArrayStack *stack, int num) {
    if (stack->size == MAX_SIZE) {
        printf("stack is full.\n");
        return;
    }
    stack->data[stack->size] = num;
    stack->size++;
}

/* get top element of stack */
int peek(ArrayStack *stack) {
    if (stack->size == 0) {
        printf("stack is empty.\n");
        return INT_MAX;
    }
    return stack->data[stack->size - 1];
}

/* pop top element of stack */
int pop(ArrayStack *stack) {
    if (stack->size == 0) {
        printf("stack is empty.\n");
        return INT_MAX;
    }
    int val = peek(stack);
    stack->size--;
    return val;
}
