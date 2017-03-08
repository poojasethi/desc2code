#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
const long long INF = 1ll<<60;
int a[8][3], tot;
long long dis[30], miv[30];

long long dist(int x, int y)
{
	long long ans = 0;
	for(int i = 0; i < 3; i++)
		ans += (long long)(a[x][i]-a[y][i])*(a[x][i]-a[y][i]);
	return ans;
}

bool judge()
{
	sort(dis, dis+28);
	int i = 1;
	long long *a = dis;
	for(; i < 12; i++)
		if(a[i] != a[i-1]) return 0;
	if(a[i] != 2*a[i-1]) return 0;
	for(i++ ; i < 24; i++)
		if(a[i] != a[i-1]) return 0;
	if(a[i] != 3*a[0]) return 0;
	for(i++; i < 28; i++)
		if(a[i] != a[i-1]) return 0;
	return a[0] != 0;
}

bool dfs(int k)
{
	if(k == 8) return judge();

	sort(a[k], a[k]+3);
	
	int ok = 1, gao;
	while(ok || next_permutation(a[k], a[k]+3)) {
		ok = 0;
		gao = 1;
		for(int i = 0; i < k; i++) {
			long long t = dist(i, k);
			if(!tot) miv[tot] = t;
			else miv[tot] = min(miv[tot-1], t);

			if(t > 3*miv[tot])
				gao = 0;
			dis[tot++] = t;
		}

		if(gao && dfs(k+1)) return 1;
		for(int i = 0; i < k; i++) tot--;

	}
	return 0;
}

int main()
{
	for(int i = 0; i < 8; i++)
		for(int j = 0; j < 3; j++)
			cin >> a[i][j];

	tot = 0;
	if(dfs(0)) {
		puts("YES");
		for(int i = 0; i < 8; i++)
			printf("%d %d %d\n", a[i][0], a[i][1], a[i][2]);
	} else puts("NO");
	return 0;
}