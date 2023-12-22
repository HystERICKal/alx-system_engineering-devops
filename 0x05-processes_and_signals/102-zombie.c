#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"

/**
 * infinite_while - a forever loop
 * Return: int
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - program entry point
 * Return: 0int
 */
int main(void)
{
	int x;
	parent_id_t parent_id;

	for (x = 0; x < 5; x++)
	{
		parent_id = fork();
		if (!parent_id)
			break;
		printf("Zombie process created, PID: %i\n", (int)parent_id);
	}
	if (parent_id != 0)
		infinite_while();
	return (0);
}
