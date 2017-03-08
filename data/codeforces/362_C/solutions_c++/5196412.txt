#include <cstdio>
int n,a[5010],f[5010][5010]={{0}},ans,g[10020]={0},x,k;
int main(){
	scanf("%d",&n);
	for (int i = 1;i <= n;i++) scanf("%d",&a[i]);
	ans = 0;
	for (int i = 1;i < n;i++)
		for (int j = i + 1;j <= n;j++) ans += (a[i] > a[j]);
	for (int i = 1; i <= n;i++)
		for (int j = 1;j <= n;j++){
			f[i][j] = f[i][j - 1];
			if (a[j] > a[i]) f[i][j]++;
		}
	k = 0;
	for (int i = 1;i < n;i++)
		for (int j = i + 1;j <= n;j++){
			x = 0;
			if (a[i] > a[j]) x++;else x--;
			x -= 2 * (f[i][j - 1] - f[i][i]);
			x += 2 * (f[j][j] - f[j][i]);
			if (x > 0) g[x]++;
			if (k < x) k = x;
		}
	printf("%d %d\n",ans - k,g[k]);
}
