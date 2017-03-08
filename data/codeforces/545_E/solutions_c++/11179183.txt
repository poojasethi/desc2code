#include <bits/stdc++.h>

using namespace std;

void optimizeIO()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
}

const int N = 3e5 + 10;

int u[N], v[N];
long long w[N];
bool vis[N];
vector<int> graph[N];
int ans[N];

int main()
{
	optimizeIO();
	int n, m;
	cin >> n >> m;
	for (int i = 1; i <= m; i++)
	{
		cin >> u[i] >> v[i] >> w[i];
		graph[u[i]].push_back(i);
		graph[v[i]].push_back(i);
	}
	int s;
	cin >> s;
	set<pair<pair<long long, long long>, pair<int, int> > > Q;
	Q.insert(make_pair(make_pair(0, -1), make_pair(-1, s)));
	long long sum = 0;
	while (!Q.empty())
	{
		pair<pair<long long, long long>, pair<int, int> > top = *Q.begin();
		Q.erase(Q.begin());
		int U = top.second.second;
		long long cdist = top.first.first;
		long long ldist = top.first.second;
		int le = top.second.first;
		if (vis[U]) continue;
		vis[U] = 1;
		if (le != -1)
		{
			ans[U] = le;
			sum += ldist;
		}
		for (int i = 0; i < (int) graph[U].size(); i++)
		{
			int e = graph[U][i];
			int W = u[e]==U?v[e]:u[e];
			Q.insert(make_pair(make_pair(cdist + w[e], w[e]), make_pair(e, W)));
		}
	}
	cout << sum << endl;
	for (int i = 1; i <= n; i++)
		if (i != s)
			cout << ans[i] << ' ';
	printf("%s", sum?"\n":"");
	return 0;
}
