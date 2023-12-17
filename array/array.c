#include <stdio.h>

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

	return 0;
}
