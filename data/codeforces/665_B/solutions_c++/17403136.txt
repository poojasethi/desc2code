#include <bits/stdc++.h>

using namespace std;

int n, m, k, a, pos[111], res;

int main()
{
	scanf("%d %d %d", &n, &m, &k);

	for (int i = 1; i <= k; ++i)
	{
		scanf("%d", &a);
		pos[a] = i;
	}

	for (int i = 0; i < n; ++i)
	for (int j = 0; j < m; ++j)
	{
		scanf("%d", &a);
		res += pos[a];
		for (int ii = 1; ii <= k; ++ii)
		if (pos[ii] < pos[a])
			++pos[ii];
		pos[a] = 1;
	}

	printf("%d", res);
	return 0;
}