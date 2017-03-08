#include <bits/stdc++.h>
using namespace std;

typedef long double db;

int n,m,x,y,a[1005];
db f[1005][1005];

int main(){
	scanf("%d%d",&n,&m);
	for(int i = 1;i <= n;i ++)	scanf("%d",&a[i]);
	for(int i = 1;i <= n;i ++)
		for(int j = 1;j <= n;j ++)
			if(i != j)	f[i][j] = (a[i] > a[j]) ? 1.0 : 0.0;
	for(int i = 1;i <= m;i ++){
		scanf("%d%d",&x,&y);
		f[x][y] = f[y][x] = 0.5;
		for(int j = 1;j <= n;j ++)	if(j != x && j != y)	f[x][j] = f[y][j] = (f[x][j] + f[y][j]) / 2.0,  f[j][x] = f[j][y] = (f[j][x] + f[j][y]) / 2.0;
	}
	db ans = 0;
	for(int i = 1;i <= n;i ++)
		for(int j = i + 1;j <= n;j ++)
			ans += f[i][j];
	printf("%.10lf\n",(double)ans);
	return 0;
}
	

