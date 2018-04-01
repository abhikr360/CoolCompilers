#include <stdio.h>

int main()
{
	int i = 0;
	if(i == 0)
	{
		int i = 1;
		printf("%d\n", i);
		if(i == 1)
		{
			//int i = 2;
			printf("%d\n", i);
		}
		printf("%d\n", i);
	}
}