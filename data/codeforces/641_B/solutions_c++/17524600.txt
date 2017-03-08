#include <bits/stdc++.h>

using namespace std;

typedef pair<int,int> pii;

int n, m, q, res[111][111];
pii pos[111][111];
int type, r, c, x;

int main()
{
	scanf("%d %d %d", &n, &m, &q);

	for (int i = 1; i <= n; ++i)
	for (int j = 1; j <= m; ++j)
		pos[i][j] = pii(i, j);

	while (q--)
	{
		scanf("%d", &type);

		if (type == 1)
		{
			scanf("%d", &r);
			for (int i = 0; i < m; ++i)
				pos[r][i] = pos[r][i+1];
			pos[r][m] = pos[r][0];
		}
		else if (type == 2)
		{
			scanf("%d", &c);
			for (int i = 0; i < n; ++i)
				pos[i][c] = pos[i+1][c];
			pos[n][c] = pos[0][c];
		}
		else
		{
			scanf("%d %d %d", &r, &c, &x);
			res[pos[r][c].first][pos[r][c].second] = x;
		}
	}

	for (int i = 1; i <= n; ++i)
	{
		for (int j = 1; j <= m; ++j)
			printf("%d ", res[i][j]);
		printf("\n");
	}
	return 0;
}