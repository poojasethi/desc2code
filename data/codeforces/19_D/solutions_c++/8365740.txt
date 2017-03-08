#include <cstdio>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;
const int maxn = 2 * 1e5 + 5;
const int INF = 0x3f3f3f3f;
#define lowbit(x) ((x)&(-x))
typedef pair<int,int> pii;
typedef set<pii>::iterator iter;

int N, M, pos[maxn];
set<pii> fenw[maxn];

struct Camd {
	int x, y;
	char op[10];
	void read() { scanf("%s%d%d", op, &x, &y); }
	void add() {
		for (int i = maxn - y; i < maxn; i += lowbit(i))
			fenw[i].insert(make_pair(x, y));
	}
	void del() {
		for (int i = maxn - y; i < maxn; i += lowbit(i))
			fenw[i].erase(make_pair(x, y));
	}
	void find() {
		pii ans(INF, INF);
		for (int i = maxn-y-1; i; i -= lowbit(i)) {
			iter it = fenw[i].lower_bound(make_pair(x+1, y));
			if (it != fenw[i].end())
				ans = min(ans, *it);
		}
		if (ans == make_pair(INF,INF))
			printf("-1\n");
		else
			printf("%d %d\n", ans.first, pos[ans.second]);
	}
	void solve() {
		if (op[0] == 'a') add();
		else if (op[0] == 'r') del();
		else find();
	}
}p[maxn];

void init () {
	M = 0;
	scanf("%d", &N);
	for (int i = 1; i <= N; i++) {
		p[i].read();
		pos[i] = p[i].y;
	}
	sort(pos + 1, pos + 1 + N);
	M = unique(pos+1, pos+1+N) - (pos+1);
	
	for (int i = 1; i <= N; i++)
		p[i].y = lower_bound(pos+1, pos+1+M, p[i].y) - pos;
}

int main () {
	init();

	for (int i = 1; i <= N; i++)
		p[i].solve();
	return 0;
}
