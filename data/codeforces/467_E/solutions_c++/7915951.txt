#include <cstdio>
#include <cstring>
#include <map>
#include <stack>
#include <vector>
#include <algorithm>

using namespace std;
const int maxn = 5 * 1e5 + 5;

int N, B[maxn];

void solve () {
	vector<int> ans;
	map<int, int> pre, sum;

	int mv = 0;
	while (mv < N) {
		pre.clear();
		sum.clear();
		stack<int> sta;

		for (int& i = mv; i < N; i++) {
			if (pre[B[i]]) {
				for (int j = 0; j < 2; j++) {
					ans.push_back(pre[B[i]]);
					ans.push_back(B[i]);
				}
				break;
			}

			while (!sta.empty() && (sum[B[i]] > 1 || (sum[B[i]] == 1 && sta.top() != B[i]))) {
				pre[sta.top()] = B[i];
				sum[sta.top()]--;
				sta.pop();
			}
			sta.push(B[i]);
			sum[B[i]]++;
		}
		mv++;
	}
	printf("%lu\n", ans.size());
	for (int i = 0; i < ans.size(); i++)
		printf("%d%c", ans[i], i == ans.size() - 1 ? '\n' : ' ');
}

int main () {
	scanf("%d", &N);
	for (int i = 0; i < N; i++)
		scanf("%d", &B[i]);
	solve();
	return 0;
}
