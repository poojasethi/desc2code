#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<cstdlib>
#include<ctime>
#include<cmath>
#include<climits>
#include<algorithm>
#include<map>
using namespace std;

#define NEXT seq[CUR]
#define N 100010
int seq[N], val[N];
bool vst[N];
int n, m;

int cmp(const int &i, const int &j) { return val[i] < val[j]; }

bool judge(int x) {
	while (x) { if (x % 10 != 4 && x % 10 != 7) return false; x /= 10; }
	return true;
}

void swapcircle(int x) {
	int CUR;
	if (x != m) printf("%d %d\n", x+1, m+1); vst[x] = 1;
	for (CUR = x; !vst[NEXT]; CUR = NEXT) {
		printf("%d %d\n", CUR+1, NEXT+1);
		vst[NEXT] = 1;
	} if (x != m) printf("%d %d\n", CUR+1, m+1); else m = CUR;
}

void conduct()
{
	int i, j, cnt;
	for (i = 0; i < n; ++i) scanf("%d", &val[i]);
	for (i = 1; i < n; ++i) if (val[i] < val[i-1]) break;
	if (i == n) { printf("0\n"); return; }
	for (i = 0; i < n; ++i) if (judge(val[i])) break;
	if (i == n) { printf("-1\n"); return; } m = i;
	for (i = 0; i < n; ++i) seq[i] = i; sort(seq, seq+n, cmp);
	memset(vst, 0, sizeof(vst)); cnt = 0;
	for (i = 0; i < n; ++i) if (!vst[i] && seq[i] != i) {
		cnt++; for (j = i; !vst[j]; j = seq[j]) { vst[j] = 1; cnt++; }
	} if (seq[m] != m) cnt -= 2; printf("%d\n", cnt);
	memset(vst, 0, sizeof(vst)); swapcircle(m);
	for (i = 0; i < n; ++i) if (!vst[i] && seq[i] != i) swapcircle(i);
}

int main()
{
	while (scanf("%d", &n) != EOF) conduct();
	return 0;
}
