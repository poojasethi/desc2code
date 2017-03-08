#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
using namespace std;

typedef long long ll;

#define endl '\n'

int N, M, a[100005];
bool vis[100005];
vector<vector<int> > e(100005);
vector<int> l;

bool dfs(int u, int p) {
	if (vis[u])
		return true;
	vis[u] = true;
	if (a[u] == u)
		p = u;
	if (a[u] != p)
		return false;
	bool poss = true;
	for (int i = 0; i < e[u].size(); ++i)
		if (!dfs(e[u][i],p))
			poss = false;
	if (poss && p == u)
		l.push_back(u);
	return poss;
}

int main() {
	ios::sync_with_stdio(false);
	cin >> N >> M;
	for (int i = 0; i < M; ++i) {
		int u, v;
		cin >> u >> v;
		e[u].push_back(v);
	}
	for (int i = 1; i <= N; ++i)
		cin >> a[i];
	for (int i = 1; i <= N; ++i) {
		if (!vis[i] && i == a[i]) {
			if (!dfs(i,i)) {
				cout << -1 << endl;
				return 0;
			}
		}
	}
	cout << l.size() << endl;
	for (int i = 0; i < l.size(); ++i)
		cout << l[i] << endl;
}