#include <stdio.h>

#define MAX_SIZE 100001
static char S[MAX_SIZE], A[MAX_SIZE];
static int B[MAX_SIZE];

int main(void)
{
	int T;
	
	scanf("%d", &T);
	while (T--)
	{
		int i, cnt, min, j;
		
		scanf("%s", S);
		cnt = 1; j = 0;
		A[j++] = S[0];
		for (i = 1; S[i]; i++)
		{
			if (S[i] == S[i-1])
			{
				cnt++;
			}
			else
			{
				B[j-1] = cnt;
				A[j++] = S[i];
				cnt = 1;
			}
		}
		B[j-1] = cnt;
		min = cnt = MAX_SIZE;
		for (i = 1; i < j-1 && min > 3; i++)
		{
			if (A[i-1] != A[i+1])
			{
				cnt = B[i] + 2;
			}
			if (min > cnt)
			{	
				min = cnt;
			}
		}
		printf("%d\n", min);
	}
	
	return 0;
}
