#include <cstdio>
#include <cstring>
#include <algorithm>
#define FOR(i,j,k) for(i=j;i<=k;i++)
using namespace std;
const int N = 50005;
char str[N]={0}, ans[N];
int p[N][26], f[N][101]={0};
int main() {
	int n, i, j, k, l = 0, t;
	scanf("%s", str+1);
	t = n = strlen(str+1);
	FOR(i,1,n) str[i]-='a';
	FOR(i,1,n) memcpy(p[i],p[i-1],sizeof(p[0])),p[i][str[i]]=i;
	FOR(i,1,n) f[i][0]=i+1,f[i][1]=i;
	FOR(i,2,n) FOR(j,2,100) {
		f[i][j]=f[i-1][j];
		if (f[i-1][j-2])
			f[i][j]=max(f[i][j],p[f[i-1][j-2]-1][str[i]]);
	}
	FOR(i,0,100) if(f[n][i]) k=i;
	while (k > 1) {
		ans[l++]=str[f[t][k]]+'a';
		t=p[t][str[f[t][k]]]-1;
		k-=2;
	}
	ans[l]=0;
	printf("%s", ans);
	if(k)printf("%c",str[f[t][k]]+'a');
	reverse(ans, ans+l);
	printf("%s", ans);
	return 0;
}
