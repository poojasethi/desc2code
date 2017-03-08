#include <bits/stdc++.h>

using namespace std;

int n, a[111];

int main()
{
	scanf("%d", &n);

	for (int i = 1; i <= n; ++i)
		scanf("%d", a+i);

	for (int i = 0; i < n; ++i)
	{
		for (int j = 1; j < n; ++j)
		if (a[j] > a[j+1])
			printf("%d %d\n", j, j+1), swap(a[j], a[j+1]);
	}
	return 0;
}