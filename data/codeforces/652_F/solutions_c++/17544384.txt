#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<vector>
#include<cmath>
#define ll long long
#define ld long double
using namespace std;
const int maxn= 5e5;
pair<int,int> o[maxn];
char s[10],d[maxn];
int pos[maxn],p[maxn],f[maxn];
ll t,sh;
int n,m,i,j,x,y;
int main()
{
#ifndef ONLINE_JUDGE	
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
#endif
	scanf("%d%d%I64d",&n, &m, &t);
	for (i= 1;i<=n;i++){
		scanf("%d%s",&pos[i], s+1);
		d[i]= s[1];
		pos[i]--;
		o[i-1]= make_pair(pos[i],i);
	}
	sort(o,o+n);
	for (i= 0;i<n;i++)
		f[o[i].second]= i;
	for (i= 1;i<=n;i++){
		int dir= d[i]=='L'?-1:1;
		ll des= pos[i]+t*dir;
		if (des>0) sh+= des/m;
		else sh+= (des-m+1)/m;
		p[i-1]= (des%m+m)%m;
	}
	sh= (sh%n+n)%n;	
	sort(p,p+n);
	for (i= 1;i<=n;i++)
		printf("%d%c",p[(f[i]+sh)%n]+1,i<n?' ':'\n');
	return 0;
}
