#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<climits>
#include<algorithm>
#include<vector>
#include<string>
#include<queue>
#include<deque>
#include<set>
#include<map>
using namespace std;

#define N 1010
char name[N][110];
int exp[N][2], lis[N][2], val[N], pre[N], pro[N], sp[N][N], d[N][N];
int n, m, tot;

void conduct()
{
	int i, j, t, pt, pos, cur;
	for (i = 0; i < n; ++i) scanf("%d%d%d%d", &exp[i][0], &lis[i][0], &exp[i][1], &lis[i][1]);
	scanf("%d", &m); for (i = 0; i < m; ++i) scanf("%s%d", name[i], &val[i]);
	for (i = 0; i < m; ++i) { pre[i] = i-1; pro[i] = i+1; } pre[0] = m-1; pro[m-1] = 0;
	memset(d, 0, sizeof(d)); memset(sp, 0, sizeof(sp));
	for (cur = pos = 0, pt = tot; m; cur = pro[cur]) {
		t = max(1, val[cur] - (exp[pos%n][pos/n]+lis[pos%n][1-pos/n]) - d[pos%n][cur]);
		if (t <= pt) {
			pt = pt - t; sp[pos%n][++sp[pos%n][0]] = cur;
			pro[pre[cur]] = pro[cur]; pre[pro[cur]] = pre[cur]; m--;
		} else { d[pos%n][cur] += pt; pt = 0; }
		if (!pt) { pos = (pos+1) % (2*n); pt = tot; }
	} for (i = 0; i < n; ++i) {
		printf("%d", sp[i][0]);
		for (j = 1; j <= sp[i][0]; ++j) printf(" %s", name[sp[i][j]]);
		printf("\n");
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	while (scanf("%d%d", &n, &tot) != EOF) conduct();
	fclose(stdin); fclose(stdout);
	return 0;
}
