#include <bits/stdc++.h>

using namespace std;

int n, t, r, w[400];

int main()
{
	scanf("%d %d %d", &n, &t, &r);

	for (int i = 1; i <= n; ++i)
		scanf("%d", w+i);

	if (t < r)
		return printf("-1"), 0;

	int res = 0;
	queue<int> q;

	for (int i = 1; i <= n; ++i)
	{
		while (!q.empty() && q.front() + t < w[i])
			q.pop();

		while (q.size() < r)
		{
			++res;
			q.push(w[i] - r + q.size());
		}
	}

	printf("%d", res);
	return 0;
}