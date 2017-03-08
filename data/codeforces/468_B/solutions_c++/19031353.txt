#include <bits/stdc++.h>

using namespace std;

int n, a, b, x[100010];
map<int,int> mp;
queue<int> q;

int main()
{
	scanf("%d %d %d", &n, &a, &b);

	for (int i = 0; i < n; ++i)
	{
		scanf("%d", x+i);
		mp[x[i]] = 1;
	}

	for (int i = 0; i < n; ++i)
	if (mp.find(a - x[i]) == mp.end())
		mp[x[i]] = 2, q.push(x[i]);

	while (!q.empty())
	{
		int u = q.front();
		q.pop();
		// cout << u << '\n';
		if (mp.find(b - u) == mp.end())
		{
			printf("NO");
			return 0;
		}

		if (mp[b-u] == 1)
			mp[b-u] = mp[a-b+u] = 2, q.push(a-b+u);
	}

	printf("YES\n");
	for (int i = 0; i < n; ++i)
		printf("%d ", mp[x[i]] - 1);
	return 0;
}