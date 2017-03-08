#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>
#include<cmath>
#define ll long long
using namespace std;
const ll maxn= 3e5;
struct peo{
	ll d,r,h;
}P[maxn];
struct day{
	ll t,h;
}D[maxn];
ll ans[maxn];
ll c[3][maxn];
ll n,m,i,j,k,p,q,x,y,z;
bool cmp(peo a,peo b){
	return a.d<b.d;
}
bool _cmp(day a,day b){
	return a.t<b.t;
}
ll lowbit(ll o){
	return o & -o;
}
void add(ll k,ll o,ll x){
	while(o<=m){
		c[k][o]+= x;
		o+= lowbit(o);
	}
}
ll find(ll k,ll o){
	ll re= 0;
	while (o){
		re+= c[k][o];
		o-= lowbit(o);
	}return re;
}
bool ok(ll m,ll d,ll r){
	ll x= find(1,m);
	ll sum= find(2,m);
	if (sum-x*d>=r) return 1;
	return 0;
}
int main()
{
	scanf("%lld%lld",&n, &m);
	for (i= 1;i<=m;i++){
		scanf("%lld",&D[i].t);
		D[i].h= i;
	}
	for (i= 1;i<=n;i++){
		scanf("%lld%lld",&P[i].d, &P[i].r);
		P[i].h= i;
	}
	sort(P+1,P+n+1,cmp);
	sort(D+1,D+m+1,_cmp);
	j= m;
	for (i= n;i>0;i--){
		while(j&&D[j].t>P[i].d){
			add(1,D[j].h,1);
			add(2,D[j].h,D[j].t);
			j--;
		}
		ll l= -1,r= m+1;
		while (l+1<r){
			ll mid= (l+r)>>1;
			if (ok(mid,P[i].d,P[i].r)) r= mid;
			else l= mid;
		}
		if (r==m+1) r= 0;
		ans[P[i].h]= r;
	}
	for (i= 1;i<=n;i++)
		printf("%lld%c",ans[i],i<n?' ':'\n');
	return 0;
}
