/*
ID:wysovie1
LANG:C++
TASK:
*/

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>

#define lowbit(x) ((x) & (-(x)))
#define REP(i, a) for (int i = 0; i < a; i++)
#define REPD(i, a) for (int i = a - 1; ~i; i--)
#define TR(it, a) for (__typeof(a.begin()) it = a.begin(); it != a.end(); ++it)
#define PB(i) push_back(i)
#define MS(a, i) memset(a, i, sizeof(a))
#define MP(a, b) make_pair(a, b)
#define ALL(a) a.begin(),a.end()
#define DEB(x) cout << #x << " : " << x << endl
#define DEBA(a, n) REP(i, n) cout << #a << "[" << i << "] : " << a[i] << endl
#define FI first
#define SE second

using namespace std;

const int maxn = 1e5+10;
int i, j, k, n, m, f, a[maxn], b[maxn], q[maxn], z[maxn];
vector<int> e[maxn];
vector<int> s[maxn];

int get(int k, int x) {
	int ret = 0;
	for (; x; x -= lowbit(x)) 
		ret += s[k][x];
	return ret;
}

int add(int k, int x, int t) {
	for (; x < s[k].size(); x += lowbit(x))
		s[k][x] += t;
}

int main() {
	cin >> n;
	for (int i = 1; i <= n - 1; i++) {
		scanf("%d%d", a + i, b + i);
		e[a[i]].PB(b[i]);
		e[b[i]].PB(a[i]);
	}
	
	int r = 1;
	REP(i, n + 1) if (e[i].size() > 2)
		r = i;

	REP(i, e[r].size()) {
		for (j = e[r][i], f = r, k = 0;;) {
			q[j] = ++k, z[j] = i;
			if (e[j].size() == 1) break;
			m = f, f = j, j = e[f][0];
			if (j == m) j = e[f][1];
		}
		s[i].resize(k + 1, 0);
	}
	
	scanf("%d", &m);
	while (m--) {
		int k, i;
		scanf("%d%d", &k, &i);
		if (k < 3) add(max(z[a[i]],z[b[i]]), max(q[a[i]],q[b[i]]), k*2-3);
	 	else { scanf("%d", &j);
			if (z[i] == z[j]) printf("%d\n", get(z[i], q[i]) == get(z[j], q[j])?abs(q[i]-q[j]):-1);
			else printf("%d\n", get(z[i],q[i])+get(z[j],q[j])?-1:q[i]+q[j]);
		}
	}

	return 0;
}

