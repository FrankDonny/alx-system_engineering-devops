#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * infinite_while - runs an infinite loop of sleep function
 * Return: 0 on success
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
 * main - creates a zombie process
 * Return: 0 on success
 */
int main(void)
{
	int num_of_processes, new;

	for (num_of_processes = 0; num_of_processes < 5; num_of_processes++)
	{
		new = fork();
		if (new > 0)
		{
			printf("Zombie process created, PID: %d\n", new);
			sleep(1);
		}
	}

	infinite_while();

	return (0);
}
