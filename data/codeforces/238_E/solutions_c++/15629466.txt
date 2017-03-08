#include <stdio.h>
#include <string.h>
#include <vector>
using namespace std;
vector<int> u[101][101];
int dis[101][101];
int fr[101], to[101];
int ans[101], c[101];
int main()
{
	int n, m, a, b;
	scanf("%d%d%d%d", &n ,&m, &a, &b);
	memset(dis, 0x23, sizeof(dis));
	memset(ans, 0x23, sizeof(ans));
	for (int i = 0; i < m; i++)
	{
		int u, v;
		scanf("%d%d", &u, &v);
		dis[u][v] = 1;
	}
	for (int i = 1; i <= n; i++)
		dis[i][i] = 0;
	for (int k = 1; k <= n; k++)
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++)
				if (dis[i][k] + dis[k][j] < dis[i][j])
					dis[i][j] = dis[i][k] + dis[k][j];
	int d;
	scanf("%d", &d);
	for (int i = 0; i < d; i++)
	{
		int s, t;
		scanf("%d%d", &s, &t);
		fr[i] = s, to[i] = t;
		if (dis[s][t] > 10101)
			continue;
		for (int j = 0; j <= dis[s][t]; j++)
			for (int k = 1; k <= n; k++)
				if (dis[s][k] == j && dis[k][t] == dis[s][t] - j)
					u[i][j].push_back(k);
	}
	int fl = 1, nb = 0;
	ans[b] = 0;
	while (fl)
	{
		fl = 0;
		nb++;
		for (int i = 0; i < d; i++)
		{
			if (dis[fr[i]][to[i]] > 10101)
				continue;
			int s = fr[i], t = to[i];
			c[t] = ans[t];
			for (int j = dis[s][t] - 1; j >= 0; j--)
			{
				int sz = u[i][j].size();
				for (int k = 0; k < sz; k++)
				{
					int nw = u[i][j][k];
					c[nw] = 0;
					for (int l = 1; l <= n; l++)
						if (dis[nw][l] == 1 && dis[l][t] == dis[s][t] - j - 1)
							if (c[nw] < c[l])
								c[nw] = c[l];
					if (ans[nw] < c[nw])
						c[nw] = ans[nw];
				}
				if (sz == 1)
				{
					int nw = u[i][j][0];
					if (ans[nw] > 10101 && c[nw] < nb)
						ans[nw] = nb, fl = 1;
				}
			}
		}
		if (ans[a] < 10101)
			fl = 0;
	}
	printf("%d", ans[a] < 10101 ? ans[a] : -1);
}
