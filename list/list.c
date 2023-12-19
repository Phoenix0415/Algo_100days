/* constructor of list */
MyList *newMyList() {
    MyList *nums = malloc(sizeof(MyList));
    nums->capacity = 10;
    nums->arr = malloc(sizeof(int) * nums->capacity);
    nums->size = 0;
    nums->extendRatio = 2;
    return nums;
}

/* destructor of list */
void delMyList(MyList *nums) {
    free(nums->arr);
    free(nums);
}

/* get size of list */
int size(MyList *nums) {
    return nums->size;
}

/* get capacity of list */
int capacity(MyList *nums) {
    return nums->capacity;
}

/* get element */
int get(MyList *nums, int index) {
    assert(index >= 0 && index < nums->size);
    return nums->arr[index];
}

/* set element */
void set(MyList *nums, int index, int num) {
    assert(index >= 0 && index < nums->size);
    nums->arr[index] = num;
}

/* add element at the end */
void add(MyList *nums, int num) {
    if (size(nums) == capacity(nums)) {
        extendCapacity(nums); // extend capacity
    }
    nums->arr[size(nums)] = num;
    nums->size++;
}

/* insert element at the index */
void insert(MyList *nums, int index, int num) {
    assert(index >= 0 && index < size(nums));
    // index out of range, trigger extension of capacity
    if (size(nums) == capacity(nums)) {
        extendCapacity(nums); // extend capacity
    }
    for (int i = size(nums); i > index; --i) {
        nums->arr[i] = nums->arr[i - 1];
    }
    nums->arr[index] = num;
    nums->size++;
}

/* remove element at the index */
// note: `remove` is a keyword in C++, so we use `removeItem` instead of `remove`
int removeItem(MyList *nums, int index) {
    assert(index >= 0 && index < size(nums));
    int num = nums->arr[index];
    for (int i = index; i < size(nums) - 1; i++) {
        nums->arr[i] = nums->arr[i + 1];
    }
    nums->size--;
    return num;
}

/* extend capacity */
void extendCapacity(MyList *nums) {
    // allocate new memory
    int newCapacity = capacity(nums) * nums->extendRatio;
    int *extend = (int *)malloc(sizeof(int) * newCapacity);
    int *temp = nums->arr;

    // copy old data to new memory
    for (int i = 0; i < size(nums); i++)
        extend[i] = nums->arr[i];

    // free old memory
    free(temp);

    // update capacity
    nums->arr = extend;
    nums->capacity = newCapacity;
}

/* convert list to array */
int *toArray(MyList *nums) {
    return nums->arr;
}