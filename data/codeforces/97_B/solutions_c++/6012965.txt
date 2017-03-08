#include <cstdio>
#include <algorithm>
#define mp make_pair
#define fir first
#define sec second
using namespace std;
const int N = 10005;
pair<int, int> a[N], b[N*15];
int n, cnt;
void solve(int l, int r) {
	int ml = (l + r) >> 1, mr = ml, mx = a[ml].fir;
	for (; ml>=l && a[ml].fir==mx; --ml);
	for (; mr<=r && a[mr].fir==mx; ++mr);
	for (int i=l; i<=r; ++i) b[++cnt] = mp(mx, a[i].sec);
	if (l <= ml) solve(l, ml);
	if (mr <= r) solve(mr, r);
}
int main() {
	scanf("%d", &n);
	for (int i=1; i<=n; ++i)
		scanf("%d%d", &a[i].fir, &a[i].sec);
	sort(a+1, a+n+1);
	solve(1, n);
	sort(b+1, b+cnt+1);
	cnt = unique(b+1, b+cnt+1) - b - 1;
	printf("%d\n", cnt);
	for (int i=1; i<=cnt; ++i)
		printf("%d %d\n", b[i].fir, b[i].sec);
	return 0;
}