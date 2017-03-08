#include <cstdio>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

const int MAXN = 100010;

int n, a, b, k[MAXN];
vector<int> adj[MAXN];

long long gao(int i, int src) {
	vector< pair<long long, int> > v;
	for (int j = 0; j < adj[i].size(); ++j) {
		int ii = adj[i][j];
		if (ii != src) {
			--k[ii];
			v.push_back(make_pair(gao(ii, i), ii));
			++k[ii];
		}
	}
	sort(v.begin(), v.end(), greater< pair<long long, int> >());
	long long ret = 0, sum = 0;
	for (int j = 0; j < v.size() && k[i] >= 1; ++j) {
		ret += 1 + v[j].first + 1;
		--k[v[j].second];
		--k[i];
		sum += k[v[j].second];
	}
	long long add = min(1LL * k[i], sum);
	ret += add * 2LL;
	k[i] -= add;
	return ret;
}

int main() {
	while (scanf("%d", &n) != EOF) {
		for (int i = 1; i <= n; ++i) {
			scanf("%d", &k[i]);
			adj[i].clear();
		}
		for (int i = 0; i < n - 1; ++i) {
			scanf("%d%d", &a, &b);
			adj[a].push_back(b);
			adj[b].push_back(a);
		}
		scanf("%d", &a);
		cout << gao(a, -1) << endl;
	}	
	return 0;
}
