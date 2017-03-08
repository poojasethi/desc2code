#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<vector>
#define ll long long
using namespace std;
const ll maxn= 5e5+10,maxm=4*maxn;
vector<int> g[maxm];
ll root,s[maxm],left[maxm],right[maxm];
ll d[100];
ll z[maxm];
ll c[maxm],a[maxm][2],Y[maxm];
ll x,y,n,m,i,j,ans,tot,L,R,top;
void dfs(ll o,ll fa){
	a[o][0]= ++tot;
	Y[tot]= o;
	ll len= g[o].size(),i;
	for (i= 0;i<len;i++){
		ll v= g[o][i];
		if (v==fa) continue;
		dfs(v,o);
	}
	a[o][1]= ++tot;
	Y[tot]= o;
}
void update(ll o){
	ll l= left[o],r= right[o];
	ll x= z[l],y= z[r];
	if (x==0) x= s[l];
	if (y==0) y= s[r];
	s[o]= x|y;
}
void pushdown(ll o){
	if (z[o]==0) return;
	ll l= left[o],r= right[o];
	z[l]= z[o];
	z[r]= z[o];
	z[o]= 0;
}
void build(ll &o,ll l,ll r){
	if (!o) o= ++top;
	if (l+1==r){
		s[o]= d[c[Y[l]]];
		return;
	}
	ll mid= (l+r)>>1;
	build(left[o],l,mid);
	build(right[o],mid,r);
	update(o);
}
void change(ll o,ll l,ll r,ll x,ll y,ll v){
	if (x<=l&&r<=y){
		z[o]= d[v];
		return;
	}
	pushdown(o);
	ll mid= (l+r)>>1;
	if (x<mid)
		change(left[o],l,mid,x,y,v);
	if (mid<y)
		change(right[o],mid,r,x,y,v);
	update(o);
}
ll ok(ll o,ll l,ll r,ll x,ll y){
	if (x<=l&&r<=y){
		if (z[o]==0) return s[o];
		return z[o];
	}
	pushdown(o);
	ll mid= (l+r)>>1,re= 0;
	if (x<mid)
		re|= ok(left[o],l,mid,x,y);
	if (mid<y)
		re|= ok(right[o],mid,r,x,y);
	update(o);
	return re;
}
int main()
{
	//freopen("1.in","r",stdin);
	//freopen("1.out","w",stdout);
	d[1]= 1;
	for (i= 2;i<=60;i++)
		d[i]= d[i-1]*2;
	scanf("%I64d%I64d",&n, &m);
	for (i= 1;i<=n;i++) scanf("%I64d",&c[i]);
	for (i= 1;i<n;i++){
		scanf("%I64d%I64d",&x, &y);
		g[x].push_back(y);
		g[y].push_back(x);
	}
	dfs(1,0);
	L= 1;R= tot+1;
	top= 0;
	build(root,L,R);
	for (ll mm= 1;mm<=m;mm++){
		scanf("%I64d",&x);
		if (x==1){
			scanf("%I64d%I64d",&x, &y);
			change(root,L,R,a[x][0],a[x][1]+1,y);
		}else {
			scanf("%I64d",&x);
			ans= 0;
			y= ok(root,L,R,a[x][0],a[x][1]+1);
			while (y){
				ans+= y&1;
				y>>= 1;
			}
			printf("%I64d\n",ans);
		}
	}return 0;
}
