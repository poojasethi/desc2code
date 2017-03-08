#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>
#include<cmath>
#define ll long long
using namespace std;
const ll maxn= 3e5,oo= 2e9;
struct item{
	ll v,h;
}E[maxn];
ll a[3][maxn],t[maxn],c[maxn],e[maxn];
ll d[3],p[3];
ll n,m,k,s,i,j;
bool cmp(item a,item b){
	return a.v<b.v;
}
int main()
{	
	scanf("%lld%lld%lld%lld",&n, &m, &k, &s);
	d[1]= d[2]= oo;
	for (i= 1;i<=n;i++){
		scanf("%lld",&a[1][i]);
		d[1]= min(d[1],a[1][i]);
	}
	for (i= 1;i<=n;i++){
		scanf("%lld",&a[2][i]);
		d[2]= min(d[2],a[2][i]);
	}
	for (i= 1;i<=m;i++){
		scanf("%lld%lld",&t[i], &c[i]);
		e[i]= d[t[i]]*c[i];
	}
	sort(e+1,e+m+1);
	ll sum= 0;
	for (i= 1;i<=k;i++)
		sum+= e[i];
	if (sum>s){
		printf("-1\n");
		return 0;
	}
	ll l= 0,r= n;
	while (l+1<r){
		ll mid= (l+r)>>1;
		d[1]= d[2]= oo;
		for (i= 1;i<=mid;i++)
			for (j= 1;j<=2;j++)
				d[j]= min(d[j],a[j][i]);
		for (i= 1;i<=m;i++)
			e[i]= d[t[i]]*c[i];
		sort(e+1,e+m+1);
		sum= 0;
		for (i= 1;i<=k;i++)
			sum+= e[i];
		if (sum>s) l= mid;
		else r= mid;
	}
	ll mid= r;
	d[1]= d[2]= oo;
	for (i= 1;i<=mid;i++)
		for (j= 1;j<=2;j++){
			if (a[j][i]<d[j]){
				d[j]= a[j][i];
				p[j]= i;
			}
		}
	for (i= 1;i<=m;i++)
		E[i]= (item){d[t[i]]*c[i],i};
	sort(E+1,E+m+1,cmp);
	printf("%lld\n",r);
	for (i= 1;i<=k;i++){
		ll h= E[i].h;
		printf("%lld %lld\n",h, p[t[h]]);
	}
	return 0;
}
