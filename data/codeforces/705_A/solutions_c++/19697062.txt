#include <stdio.h>

int main()
{
	int n, i;
	scanf("%d", &n);
	for(i=1; i<=n; i++)	{
		if(i>1)	printf("that ");
		printf("I ");
		if(i & 1)	printf("hate ");
		else	printf("love ");
	}
	printf("it\n");
	return 0;
}