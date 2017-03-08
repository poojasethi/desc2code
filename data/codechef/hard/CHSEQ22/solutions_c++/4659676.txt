// Rain Dreamer MODEL
// iSea @ 2014-08-29 00:03
// Comment - 

#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <bitset>
#include <queue>
#include <map>
#include <set>

using namespace std;

// Self Template Code BGEIN

#define sz(x) ((int)((x).size()))
#define out(x) printf(#x" %d\n", x)
#define rep(i,n) for (int i = 0; i < (n); ++i)
#define repf(i,a,b) for (int i = (a); i <= (b); ++i)
#define repd(i,a,b) for (int i = (a); i >= (b); --i)
#define repcase int t, Case = 1; for (scanf ("%d", &t); t; --t)
#define repeach(i,x) for (__typeof((x).begin()) i = (x).begin(); i != (x).end(); ++i)

typedef long long int64;
typedef pair<int, int> pii;

int sgn(double x) { return (x > 1e-8) - (x < -1e-8); }
int count_bit(int x) { return x == 0? 0 : count_bit(x >> 1) + (x & 1); }

template<class T> inline void ckmin(T &a, const T b) { if (b < a) a = b; }
template<class T> inline void ckmax(T &a, const T b) { if (b > a) a = b; }

// Self Template Code END

const int MOD = 1000000007;
const int MAXN = 100000 + 10;

struct disjoint_set {
	int p[MAXN];

	void clear(int n) {
		repf (i, 0, n) {
			p[i] = i;
		}
	}
	int find(int x) {
		return x == p[x]? x : p[x] = find(p[x]);
	}
	bool join(int x, int y) {
		x = find(x); y = find(y);
		if (x == y) {
			return false;
		}
		p[y] = x;
		return true;
	}
} ds;

int main() {
	int n, m, v, u;
	while (scanf ("%d%d", &n, &m) != EOF) {
		ds.clear(n);
		int ret = 1;
		rep (i, m) {
			scanf ("%d%d", &u, &v);
			if (ds.join(u - 1, v)) {
				ret = ret * 2 % MOD;
			}
		}
		printf ("%d\n", ret);
	}
	return 0;
}