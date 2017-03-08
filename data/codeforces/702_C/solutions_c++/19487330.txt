#include <bits/stdc++.h>

using namespace std;

int n, m, a[100010], b[100010], res;

int main()
{
	scanf("%d %d", &n, &m);

	for (int i = 0; i < n; ++i)
		scanf("%d", a+i);

	for (int i = 0; i < m; ++i)
		scanf("%d", b+i);

	for (int i = 0; i < n; ++i)
	{
		int pos = lower_bound(b, b+m, a[i]) - b;
		int tmp = 2e9;
		if (pos != m)
			tmp = min(tmp, abs(b[pos] - a[i]));
		if (pos != 0)
			tmp = min(tmp, abs(a[i] - b[pos-1]));
		res = max(res, tmp);
	}

	printf("%d\n", res);
	return 0;
}