#include <stdio.h>
int main()
{
	int n;
	scanf("%d", &n);
	if (n == 4)
	{
		printf("-1");
		return 0;
	}
	for (int i = 0; i < n; i++, printf("\n"))
		for (int j = 0; j < n; j++)
		{
			int ans;
			if (i == j)
				ans = 0;
			else if (i == (j + n - 1) % n)
				ans = 1;
			else if (i == (j + 1) % n)
				ans = 0;
			else if (((i ^ j) & 1) ^ (i < j))
				ans = 1;
			else
				ans = 0;
			printf("%d ", ans);
		}
}
