#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;
typedef pair<int, int> pii;
const int maxn = 1e5;

bool iscomp[maxn+5], vis[maxn+5];

void prime_table(int n) {
	for (int i = 2; i * i <= n; i++) {
		if (iscomp[i])
			continue;
		for (int j = i * i; j <= n; j += i)
			iscomp[j] = 1;
	}
}

int main () {
	int n;
	scanf("%d", &n);
	prime_table(n);

	vector<int> g;
	vector<pii> ans;

	for (int i = n / 2; i > 1; i--) {
		if (iscomp[i])
			continue;
		g.clear();

		for (int j = i; j <= n; j += i) {
			if (vis[j] == 0)
				g.push_back(j);
		}
		if (g.size() & 1)
			swap(g[1], g[g.size()-1]);
		for (int i = 0; i < g.size() - 1; i += 2) {
			ans.push_back(make_pair(g[i], g[i+1]));
			vis[g[i]] = vis[g[i+1]] = 1;
		}
	}

	printf("%lu\n", ans.size());
	for (int i = 0; i < ans.size(); i++)
		printf("%d %d\n", ans[i].first, ans[i].second);
	return 0;
}
