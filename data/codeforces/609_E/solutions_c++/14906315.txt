#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>
#include<cmath>
#define ll long long
using namespace std;
const ll maxn= 3e5,M= 19;
struct edge{
	ll u,v,w,h;
	edge(ll u= 0,ll v= 0,ll w= 0,ll h= 0):
		u(u),v(v),w(w),h(h){}
}L[maxn];
vector<edge> g[maxn];
ll f[maxn],d[maxn],b[maxn],F[maxn][M+1],S[maxn][M+1];
ll ans[maxn];
ll n,m,i,j,cnt,base,x;
bool cmp(edge a,edge b){
	return a.w<b.w;
}
ll find(ll o){
	if (o==f[o]) return o;
	return f[o]= find(f[o]);
}
void dfs(ll o,ll depth){
	d[o]= depth;
	ll len= g[o].size(),i;
	for (i= 0;i<len;i++){
		ll v= g[o][i].v;
		if (v==F[o][0]) continue;
		F[v][0]= o;
		S[v][0]= g[o][i].w;
		dfs(v,depth+1);
	}
}
ll get(ll x,ll y){
	if (d[x]<d[y]) swap(x,y);
	ll i,re= 0;
	for (i= M;i>=0;i--)
		if (d[F[x][i]]>=d[y]){
			re= max(re,S[x][i]);
			x= F[x][i];
		}
	if (x==y) return re;
	for (i= M;i>=0;i--)
		if (F[x][i]!=F[y][i]){
			re= max(re,S[x][i]);
			re= max(re,S[y][i]);
			x= F[x][i];
			y= F[y][i];
		}
	re= max(re,S[x][0]);
	re= max(re,S[y][0]);
	return re;
}
int main()
{
	scanf("%lld%lld",&n, &m);
	for (i= 1;i<=m;i++){
		scanf("%lld%lld%lld",&L[i].u, &L[i].v, &L[i].w);
		L[i].h= i;
	}
	sort(L+1,L+m+1,cmp);
	for (i= 1;i<=n;i++)
		f[i]= i;
	for (i= 1;i<=m;i++){
		ll u= L[i].u,v= L[i].v,w= L[i].w;
		find(u);find(v);
		if (f[u]==f[v]) continue;
		f[f[u]]= f[v];
		cnt++;
		base+= w;
		g[u].push_back((edge){u,v,w});
		g[v].push_back((edge){v,u,w});
		b[L[i].h]= 1;
		if (cnt==n-1) break;		
	}
	dfs(1,1);
	for (i= 1;i<=M;i++)
		for (j= 1;j<=n;j++){
			F[j][i]= F[F[j][i-1]][i-1];
			S[j][i]= max(S[j][i-1],S[F[j][i-1]][i-1]);
		}
	for (i= 1;i<=m;i++){
		ll h= L[i].h;
		ans[h]= base;
		if (!b[h]){
			x= get(L[i].u,L[i].v);
			ans[h]= base-x+L[i].w;
		}
	}
	for (i= 1;i<=m;i++)
		printf("%lld\n",ans[i]);
	return 0;
}
