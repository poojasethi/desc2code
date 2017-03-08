#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
const int inf=1000000000;
struct edge{
	int t,next,v,rev,c;
}g[5001];
int i,j,k,n,m,tot,ans,tmp,h[501],dis[501],l[501],fa[501],q[501],now,fv[501];
void addedge(int x,int y,int z){
	g[++tot].t=y;g[tot].next=h[x];h[x]=tot;g[tot].v=g[tot].c=z;g[tot].rev=tot+1;
	g[++tot].t=x;g[tot].next=h[y];h[y]=tot;g[tot].v=g[tot].c=z;g[tot].rev=tot-1;
}
bool bfs(int s,int t){
	int i,j,l,r;
	memset(dis,-1,sizeof(dis));
	q[1]=s;l=0;r=1;dis[s]=1;
	while (l<r){
		j=q[++l];
		for (i=h[j];i;i=g[i].next)
		 if (g[i].v&&dis[g[i].t]==-1){
		 	dis[g[i].t]=dis[j]+1;q[++r]=g[i].t;
			if (t==g[i].t) return 1;
		 }
	}
	return 0;
}
int work(int x,int t,int low){
	int res=0,i,k;
	if (x==t) return low;
	for (i=l[x];i&&low;i=g[i].next)
	 if (g[i].v&&dis[g[i].t]==dis[x]+1&&l[g[i].t]){
	 	k=work(g[i].t,t,min(low,g[i].v));
	 	res+=k;low-=k;g[i].v-=k;g[g[i].rev].v+=k;
	 	if (low) l[x]=i;
	 }
	return res;
}
int getflow(int s,int t){
	int i,res;
	for (i=1;i<=tot;i++) g[i].v=g[i].c;
	for (res=0;bfs(s,t);){
		memcpy(l,h,sizeof(h));
		res+=work(s,t,inf);
	}
	return res;
}
void dfs(int x,int fa){
	int i;
	for (i=h[x];i;i=g[i].next)
	 if (fa!=g[i].t&&!g[i].v){
	 	if (!now||g[now].c>g[i].c) now=i;
	 	dfs(g[i].t,x);
	 }
}
void solve(int x){
	int k;
	now=0;dfs(x,0);
	if (!now){
		printf("%d ",x);return;
	}
	k=now;g[k].v=g[g[k].rev].v=1;
	solve(g[k].t);solve(g[g[k].rev].t);
}
int main(){
	scanf("%d%d",&n,&m);memset(h,0,sizeof(h));tot=0;
	for (i=1;i<=m;i++) scanf("%d%d%d",&j,&k,&tmp),addedge(j,k,tmp);
	for (i=1;i<=n;i++) fa[i]=1;
	for (ans=0,i=2;i<=n;i++){
		k=getflow(i,fa[i]);ans+=k;fv[i]=k;
		bfs(i,-1);
		for (j=i+1;j<=n;j++)
		 if (dis[j]!=-1&&fa[j]==fa[i]) fa[j]=i;
	}
	tot=0;memset(h,0,sizeof(h));
	for (i=2;i<=n;i++) addedge(fa[i],i,fv[i]),g[tot].v=g[tot-1].v=0;
	printf("%d\n",ans);
	solve(1);
	puts("");
	return 0;
}