#include <cstdio>
#include <cstring>
int f[10] = {0},t,g[10] = {0},ans,l;
char s[210];
int main(){
	scanf("%d%s",&t,s);
	l = strlen(s);
	for (int i = 0;i < l;i++) f[s[i] - '0']++;
	f[2] += f[5];
	f[5] = 0;
	f[6] += f[9];
	f[9] = 0;
	while (t){
		g[t % 10]++;
		t /= 10;
	}
	g[2] += g[5];
	g[5] = 0;
	g[6] += g[9];
	g[9] = 0;
	ans = l;
	for (int i = 0;i < 10;i++) if (g[i] && ans > f[i] / g[i]) ans = f[i] / g[i];
	printf("%d",ans);
}
