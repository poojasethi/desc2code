#include <bits/stdc++.h>
using namespace std;
#define PI 2*acos(0.0)
#define INF 1e8
#define EPSILON 1e-8
#ifdef DEBUG
#define DPRINTF(x) printf x
#else
#define DPRINTF(x) ;
#endif

typedef pair<int, int> pii;
typedef pair<int, pair<int, int> > piii;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<bool> vb;
typedef vector<string> vs;

const int dx[4] = {0, 0, 1, -1}, dy[4] = {1, -1, 0, 0};
int n, m, a[1000001], b[1001][1001], Left;
bool v[1001][1001];
long long k;

inline bool isSafe(int y, int x) {
	return y>=0 && x>=0 && y<n && x<m;
}

int dfs(int y, int x, int to) {
	v[y][x] = true;
	int ret = 1;
	for (int d=0; d<4; ++d) {
		int ny=y+dy[d], nx=x+dx[d];
		if (isSafe(ny, nx) && !v[ny][nx] && b[ny][nx] >= to)
			ret += dfs(ny, nx, to);
	}
	return ret;
}

void pdfs(int y, int x, int to) {
	v[y][x] = true;

	if (Left <= 0) b[y][x] = 0;
	--Left;
	
	for (int d=0; d<4; ++d) {
		int ny=y+dy[d], nx=x+dx[d];
		if (isSafe(ny, nx) && !v[ny][nx] && b[ny][nx] >= to)
			pdfs(ny, nx, to);
	}
}

bool check(int to, int num) {
	memset(v, false, sizeof(v));
	for (int i=0; i<n; ++i) for (int j=0; j<m; ++j) {
		if (b[i][j] == to) {
			if (dfs(i, j, to) >= num) {
				memset(v, false, sizeof(v));
				Left = num;
				pdfs(i, j, to);
				printf("YES\n");
				for (int ii=0; ii<n; ++ii) {
					for (int jj=0; jj<m; ++jj)
						printf("%d ", v[ii][jj] && b[ii][jj] >= to ? to : 0);
					puts("");
				}
				exit(0);
			}
		}
	}
	return false;
}

int main () {
	scanf("%d%d%lld", &n,&m,&k);
	for (int i=0; i<n; ++i) for (int j=0; j<m; ++j) {
		scanf("%d", &b[i][j]);
		a[i*m+j] = b[i][j];
	}

	sort(a, a+n*m);
	for (int i=0; i<n*m; ++i) {
		int num = n*m-i;
		if (k%num == 0 && k/num <= a[i]) {
			check(k/num, num);
		}
	}
	printf("NO\n");
	return 0;
}


