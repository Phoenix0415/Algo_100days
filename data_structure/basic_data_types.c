#include <stdio.h>
#include <stdbool.h>

int main(void)
{
	// initialize arrays using various data types
	int	numbers[10] = {0};        // Initialize with zeros
	float	decimals[10] = {0.0};     // Initialize with zeros
	char	characters[10] = {'\0'};  // Initialize with null characters
	bool	bools[10] = {false};      // Initialize with false values
	
	printf("numbers: ");
	for (int i = 0; i < 10; i++) 
	{
        	printf("%d ", numbers[i]);
	}
    	printf("\n");
	
	printf("decimals: ");
	for (int i = 0; i < 10; i++)
	{
		printf("%f ",decimals[i]);
	}
	printf("\n");

	printf("characters: ");
    	for (int i = 0; i < 10; i++)
	{
        	printf("%c ", characters[i]);
    	}
    	printf("\n");

    	printf("bools: ");
    	for (int i = 0; i < 10; i++)
	{
        	printf("%d ", bools[i]);
    	}
    	printf("\n");

	return 0;
}
