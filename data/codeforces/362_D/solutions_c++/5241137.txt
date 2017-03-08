#include <queue>
#include <cstdio>
#include <algorithm>
#define maxn 100005
using namespace std;

struct st
{
	int x,v;
	bool operator <(const st&B) const {return v>B.v;}
};
int N,M,P,Q,S,X,Y,f[maxn],g[maxn],x[maxn],w[maxn];
priority_queue<st> F;

int find(int x) {return x==f[x]?x:f[x]=find(f[x]);}

int main()
{
	scanf("%d%d%d%d",&N,&M,&P,&Q);
	for (int i=1; i<=N; i++) f[i]=i;
	for (int i=1,y,u,v; i<=M; i++)
	{
		scanf("%d%d%d",&x[i],&y,&w[i]),X=x[i],Y=y;
		if ((u=find(x[i]))!=(v=find(y))) f[u]=v;
	}
	st u,v;
	for (int i=1; i<=M; i++) g[find(x[i])]=min(g[find(x[i])]+w[i],int(1e9));
	for (int i=1; i<=N; i++) if (f[i]==i) S++,u.x=i,u.v=g[i],F.push(u);
	if (Q>S||Q<S-P||(P&&Q==N)) {puts("NO"); return 0;}
	puts("YES");
	for (int i=1; i<=P; i++) if (S==Q) printf("%d %d\n",X,Y);
	else
	{
		u=F.top(),F.pop(),v=F.top(),F.pop(),u.v=min(2ll*(u.v+v.v)+1,1ll*int(1e9));
		F.push(u),S--,printf("%d %d\n",X=u.x,Y=v.x);
	}
}