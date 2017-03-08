#include <cstdio>
#include <cstring>
#define FOR(i,j,k) for(i=j;i<=k;i++)
char s[200001];
int c[200001];
int main() {
	scanf("%s", s + 1);
	int i, n = strlen(s + 1), m, x;
	scanf("%d", &m);
	FOR(i,1,m) scanf("%d",&x),c[x]++,c[n-x+2]--;
	FOR(i,2,n) c[i]+=c[i-1];
	FOR(i,1,n) putchar((c[i]&1)?s[n-i+1]:s[i]);
	return 0;
}