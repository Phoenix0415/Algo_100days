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

/* array traverse */
int traverse(int *nums, int size)
{
	int count = 0;
	// traverse the array using indice
	for (int i = 0; i < size; i++)
		count += nums[i];
	return count;
}

/* find an element in the array */
int find(int *nums, int size, int target)
{
	for (int i = 0; i < size; i++)
	{
		if (nums[i] == target)
			return i;
	}
	return -1;
}

/* extand the length of the array */
int *extend(int *nums, int size, int enlarge)
{
	// initialize an extended array
	int *res = (int *)malloc((size + enlarge) * sizeof(int));
	//copy all the elements to the new array
	for (int i = 0; i < size; i++)
		res[i] = nums[i];
	// initialize the extended elemens
	for (int i = size; i < size + enlarge; i++)
		res[i] = 0;
	return res;
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
	printf("the sum of all elements in the array is : %d\n", traverse(nums, 4));
	
	/* print the result of find founction */
	printf("find 5 in the nums, its index is(-1 if hasn't been found): %d\n", find(nums, 4, 5));
	
	/* print array after extension */
	printf("extend nums by 3: ");
	int *res = extend(nums, 4, 3);
	for (int i = 0; i < 7; i++)
		printf("%d ", res[i]);
	printf("\n");

	return 0;
}
