#include <cstdio>

const int N = 200200;

int lnk[N], h[N], a[N];
int n, i, x, an;

int main()
{
	scanf("%d", &n);

	for (i = 1; i <= n; i++)
	{
		int x;
		scanf("%d", &x);
		lnk[i] = h[x];
		h[x] = i;
	}

	x = 0;
	while (x >= 0 && h[x] > 0)
	{
		a[an++] = h[x];
		h[x] = lnk[h[x]];
		++x;
		if (h[x] == 0)
			while (x > 0 && h[x] == 0)
				x -= 3;
	}

	if (an == n)
	{
		puts("Possible");
		for (i = 0; i < n; i++)
			printf("%d ", a[i]);
	}
	else
		puts("Impossible");

	return 0;
}