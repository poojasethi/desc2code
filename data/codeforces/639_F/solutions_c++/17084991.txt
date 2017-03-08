#include<stdio.h>
#include<map>
#include<algorithm>
#define N 300005
using namespace std;
map<int,int>have[N];
int u[N],v[N],S[N],U[N*3];
int n,m,i,ans,x,y,Q,ni,mi,q;
int get(int *f,int u){return f[u]==u?u:f[u]=get(f,f[u]);}
struct Tree{
	int Go[N<<1],Next[N<<1],End[N],cnt,num;
	int vis[N],f[N][19],deep[N],dfn[N],tot;
	void add(int u,int v){Go[++cnt]=v;Next[cnt]=End[u];End[u]=cnt;}
	void DFS(int x){
		vis[x]=num;dfn[x]=++tot;
		for (int i=1;i<=18;i++)
			f[x][i]=f[f[x][i-1]][i-1];
		for (int i=End[x],y;i;i=Next[i])
			if (!vis[y=Go[i]])
				f[y][0]=x,deep[y]=deep[x]+1,DFS(y);
  }
  int LCA(int x,int y){
  	if (deep[x]<deep[y]) swap(x,y);
  	int d=deep[x]-deep[y];
  	for (int i=0;i<=18;i++)
  		if ((d>>i)&1) x=f[x][i];
  	if (x==y) return x;
  	for (int i=18;i>=0;i--)
  		if (f[x][i]!=f[y][i]) 	
  		  x=f[x][i],y=f[y][i];
  	return f[x][0];
  }
}T;
struct Graph{
	int Q[N],vis[N],low[N],dfn[N],id[N];
	int Go[N<<1],End[N],Next[N<<1];
	int n,Case,step,cnt;
	Graph(){Case=cnt=1;}
	void Push(int v){if (vis[v]!=Case) vis[v]=Case,Q[++*Q]=v;}
	void add(int u,int v){
		Go[++cnt]=v;Next[cnt]=End[u];End[u]=cnt;
		Push(u);Push(v);
	}
	void clear(){
		for (int i=1;i<=*Q;i++)
			low[Q[i]]=dfn[Q[i]]=End[Q[i]]=0;
		cnt=1;step=*Q=0;++Case;
	}
	void DFS(int x,int Fa){
		low[x]=dfn[x]=++step;
		for (int i=End[x],y;i;i=Next[i]){
			if ((y=Go[i])==Fa) {Fa=-1;continue;}
			if (dfn[y]) {low[x]=min(low[x],dfn[y]);continue;}
			DFS(y,x);low[x]=min(low[x],low[y]);
			if (low[y]<=dfn[x]) id[get(id,y)]=get(id,x);
	  }
  }
	void tarjan(){
		for (int i=1;i<=*Q;i++) id[Q[i]]=Q[i];
		for (int i=1;i<=*Q;i++)
			if (!dfn[Q[i]]) 
        DFS(Q[i],0);
		for (int i=1;i<=*Q;i++) get(id,Q[i]);
  }
}G,H;
void key(int &x){x+=ans;x%=n;if (!x) x=n;}
inline int cmp(const int &A,const int &B){return T.dfn[A]<T.dfn[B];}
int main(){
	scanf("%d%d%d",&n,&m,&Q);
	for (i=1;i<=m;i++)
		scanf("%d%d",&x,&y),G.add(x,y),G.add(y,x);
	for (i=1;i<=n;i++) G.Push(i);G.tarjan();
	for (i=2;i<=G.cnt;i+=2){
		x=G.id[G.Go[i]];y=G.id[G.Go[i^1]];
		if (x==y) continue;if (x>y) swap(x,y);
		if (have[x].find(y)!=have[x].end()) continue;
		have[x][y]=1;T.add(x,y);T.add(y,x);
  }
	for (i=1;i<=n;i++)
		if (G.id[i]==i&&!T.vis[i])
			++T.num,T.DFS(i);
	for (q=1;q<=Q;q++){
		scanf("%d%d",&ni,&mi);*U=0;
		for (i=1;i<=ni;i++) 
			scanf("%d",&S[i]),key(S[i]),S[i]=U[++*U]=G.id[S[i]];
		for (i=1;i<=mi;i++){
			scanf("%d%d",&u[i],&v[i]);key(u[i]),key(v[i]);
			u[i]=U[++*U]=G.id[u[i]],v[i]=U[++*U]=G.id[v[i]];
	  }sort(U+1,U+*U+1,cmp);
		x=*U=unique(U+1,U+*U+1)-(U+1);
		for (i=1;i<x;i++)
			if (T.vis[U[i]]==T.vis[U[i+1]]) 
				U[++*U]=T.LCA(U[i],U[i+1]);
		sort(U+1,U+*U+1,cmp);
		*U=unique(U+1,U+*U+1)-(U+1);
		for (i=1;i<=*U;i++) H.Push(U[i]);
		for (i=2;i<=*U;i++)
			if (T.vis[U[i]]==T.vis[U[i-1]])
				x=T.LCA(U[i-1],U[i]),H.add(x,U[i]),H.add(U[i],x);
		for (i=1;i<=mi;i++)
			if (u[i]!=v[i]) 
 				H.add(u[i],v[i]),H.add(v[i],u[i]);
		H.tarjan();
		for (i=1;i<ni;i++)
			if (H.id[S[i]]!=H.id[S[i+1]]) break;
		if (i==ni) puts("YES"),ans+=q,ans%=n;else puts("NO");
		H.clear();
  }
}