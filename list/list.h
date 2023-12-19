#ifndef LIST_H
#define LIST_H

/* class of list */
typedef struct {
    int *arr;        // array of list
    int capacity;    // capacity of list
    int size;        // size of list
    int extendRatio; // the extend ratio of list
} MyList;

#endif
