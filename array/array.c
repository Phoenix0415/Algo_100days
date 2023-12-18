#include <stdio.h>
#include <stdlib.h>

/* access a random element in the array */
int randomAccess(int *nums, int size)
{

    // get a random index in range [0, size)
    int randomIndex = rand() % size;
    // get and return the number at this random index
	int randomNum = nums[randomIndex];
	return randomNum;
}

/* insert element `num` in the index `index` */
void insert(int *nums, int size, int num, int index)
{
	// move the elements including `index` and the elements after it one position backward
	for (int i = size -1; i > index; i--)
		nums[i] = nums[i-1];
	// assign `num` to the element at `index` 
	nums[index] = num;
}

/* delete the element at index `index` */
// the keyword `remove` was occupied by `stdio.h`
void removeItem(int *nums, int size, int index)
{	
	// move the element at `index` and the ones afterward one position forward
	for (int i = index; i < size; i++)
		nums[i] = nums[i + 1];
	
}

int traverse(int *nums, int size)
{
	int count = 0;
	// traverse the array using indice
	for (int i = 0; i < size; i++)
		count += nums[i];
	return count;
}

int main(void)
{
	/* initializition of arrays */
	int arr[5] = {0}; // {0,0,0,0,0}
	int nums[5] = {1, 3, 2, 5, 4};

	/* print initialized arrays out */
	printf("arr: ");
	for (int i = 0; i < 5; i ++) 
		printf("%d ", arr[i]);
	printf("\n");
	
	printf("nums: ");
	for (int i = 0; i < 5; i++)
		printf("%d ",nums[i]);
	printf("\n\n");
	
	/* access a random element in a array */
	for (int i = 0; i < 3; i++)
		printf("a random number in nums: %d\n", randomAccess(nums,5));
	printf("\n");	
	
	/* print the array after insertion */
	printf("insert 6 at index 1 in nums: ");
	insert(nums, 5, 6, 1);
	for (int i = 0; i < 5; i++)
		printf("%d ", nums[i]);
	printf("\n");
	
	/* print the array after deletion */
	printf("delete the element at index 1 in nums: ");
	removeItem(nums, 5, 1);
	for (int i = 0; i < 4; i++ )
		printf("%d ", nums[i]);
	printf("\n");
	
	
	/* print the sum of elements using traverse function */
	printf("the sum of all elements in the array is : %d\n\n", traverse(nums, 4));
	return 0;
}
