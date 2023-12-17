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

int main(void)
{
	/* initializition of arrays */
	int arr[5] = {0}; // {0,0,0,0,0}
	int nums[5] = {1, 3, 2, 5, 4};

	printf("arr: ");
	for (int i = 0; i < 5; i ++) 
	{
		printf("%d ", arr[i]);
	}
	printf("\n");
	
	printf("nums: ");
	for (int i = 0; i < 5; i++)
	{
		printf("%d ",nums[i]);
	}
	printf("\n");
	
	for (int i = 0; i < 3; i++)
	{
		printf("a random number in nums: %d\n", randomAccess(nums,5));
	}
	printf("\n");	

	return 0;
}
