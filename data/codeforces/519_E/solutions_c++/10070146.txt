#include <iostream>
#include <vector>
using namespace std;
const int MAX = 100005;
vector<int> adj[MAX];
int par[17][MAX], size[MAX], d[MAX];
void dfs(int p, int v)
{
	par[0][v] = p;
	for (int i = 1; i < 17; i++)
		par[i][v] = par[i - 1][par[i - 1][v]];
	size[v] = 1;
	for (int i = 0; i < adj[v].size(); i++)
	{
		int u = adj[v][i];
		if (u != p)
		{
			d[u] = d[v] + 1;
			dfs(v, u);
			size[v] += size[u];
		}
	}
}
int get_parent(int v, int k)
{
	for (int i = 0; i < 17; i++)
		if ((1 << i) & k)
			v = par[i][v];
	return v;
}
int lca(int u, int v)
{
	if (d[u] < d[v])
		swap(u, v);
	u = get_parent(u, d[u] - d[v]);
	if (u == v)
		return u;
	for (int i = 16; i >= 0; i--)
		if (par[i][u] != par[i][v])
		{
			u = par[i][u];
			v = par[i][v];
		}
	return par[0][v];
}
int main()
{
	ios::sync_with_stdio(false);
	int n;
	cin >> n;
	for (int i = 0; i < n - 1; i++)
	{
		int u, v;
		cin >> u >> v;
		u--;
		v--;
		adj[u].push_back(v);
		adj[v].push_back(u);
	}
	dfs(0, 0);
	int q;
	cin >> q;
	while (q--)
	{
		int u, v;
		cin >> u >> v;
		u--;
		v--;
		int p = lca(u, v);
		int dist = d[u] + d[v] - 2 * d[p];
		if (dist == 0)
		{
			cout << n << "\n";
			continue;
		}
		if (dist & 1)
		{
			cout << "0\n";
			continue;
		}
		dist /= 2;
		if (d[u] - d[p] == dist)
		{
			u = get_parent(u, dist - 1);
			v = get_parent(v, dist - 1);
			cout << n - size[u] - size[v] << "\n";
			continue;
		}
		if (d[u] - d[p] < dist)
			swap(u, v);
		p = get_parent(u, dist);
		u = get_parent(u, dist - 1);
		cout << size[p] - size[u] << "\n";
	}
	return 0;
}
