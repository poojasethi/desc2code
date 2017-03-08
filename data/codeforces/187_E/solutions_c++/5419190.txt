#include <cstdio>
#include <algorithm>
using namespace std;
typedef unsigned int usi;

const int N = 100005;
int n, l, r, s, a[N], gap[N], p[N], a1[N], a2[N];
bool u[N];
inline void R(int &x) {
	char ch = getchar(); x = 0;
	for (; ch<'0'; ch = getchar());
	for (; ch>='0'; ch=getchar()) x = x*10 + ch-'0';
}
inline bool cmp(int a, int b) {return gap[a] < gap[b];}
usi solve(int an[]) {
	usi res = a[s] + a[n] - a[1] * 2;
	int pos = 0;
	if (l < s) {
		for (int i=1; i<=l; ++i) an[++pos] = s - i;
		int t = an[pos]; an[pos] = 1;
		for (int i=2; i<=t; ++i) an[++pos] = i;
		for (int i=s+1; i<=n; ++i) an[++pos] = i;
	}
	else {
		++s;
		for (int i=s+1; i<=n; ++i)
			gap[i] = a[i] - a[i-1], p[i - s] = i, u[i] = 0;
		sort(p+1, p+n-s+1, cmp);
		int rem = l - s + 2, pw = rem;
		usi cur = 0;
		for (int i=1; i<=rem; ++i)
			cur += (usi)gap[p[i]]<<1, u[p[i]] = 1;
		usi mi = cur; int mf = n+1;
		for (int i=0; i<rem; ++i) {
			if (!u[n-i]) {
				for (; !u[p[pw]]; --pw);
				cur -= (usi)gap[p[pw]]<<1, u[p[pw--]] = 0;
				cur += gap[n-i];
			}
			else {
				u[n-i] = 0;
				cur -= gap[n-i];
			}
			if (cur < mi) mi = cur, mf = n - i;
		}
		res += mi;
		for (int i=s+1; i<=n; ++i) u[i] = 0;
		int ed = n-mf+1;
		for (int i=mf; i<=n; ++i) u[i] = 1;
		for (int i=1; ed<rem; ++i)
			if (!u[p[i]]) u[p[i]]=1, ++ed;
		for (int i=s-2; i; --i) an[++pos] = i;
		for (int i=s; i<=n; ++i) {
			for (ed=i; u[ed+1]; ++ed);
			for (int j=ed; j>=i; --j) an[++pos] = j;
			i = ed;
		}
		--s;
	}
	return res;
}
int main() {
	R(n); R(l); R(s); r = n - l - 1;
	for (int i=1; i<=n; ++i) R(a[i]);
	if (!l) {
		if (s == 1) {
			printf("%d\n", a[n]);
			for (int i=2; i<=n; ++i)
				printf("%d ", i);
		} else
			puts("-1");
	} else
	if (!r) {
		if (s == n) {
			printf("%d\n", a[n]);
			for (int i=n-1; i; --i)
				printf("%d ", i);
		} else
			puts("-1");
	}
	else {
		usi ans1, ans2;
		ans1 = solve(a1);
		for (int i=1; i<=n; ++i) a[i] = -a[i];
		reverse(a+1, a+n+1), swap(l, r); s = n + 1 - s;
		ans2 = solve(a2);
		if (ans1 < ans2) {
			printf("%u\n", ans1);
			for (int i=1; i<n; ++i)
				printf("%d ", a1[i]);
		}
		else {
			printf("%u\n", ans2);
			for (int i=1; i<n; ++i)
				printf("%d ", n-a2[i]+1);
		}
	}
	return 0;
}