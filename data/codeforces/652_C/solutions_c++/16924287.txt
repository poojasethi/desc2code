#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int n, m, lastPos[300010], p[300010], pos[300010];
ll res;

int main()
{
	scanf("%d %d", &n, &m);

	for (int i = 1; i <= n; ++i)
		scanf("%d", p+i), pos[p[i]] = i;

	for (int i = 1, u, v; i <= m; ++i)
	{
		scanf("%d %d", &u, &v);
		if (pos[u] < pos[v])
			lastPos[pos[v]] = max(lastPos[pos[v]], pos[u]);
		else
			lastPos[pos[u]] = max(lastPos[pos[u]], pos[v]);
	}

	for (int i = 1; i <= n; ++i)
	{
		lastPos[i] = max(lastPos[i], lastPos[i-1]);
		res += i - lastPos[i];
	}
// printf("\n");
	printf("%lld", res);
	return 0;
}