#include<cstdio>
#include<cstring>
#define N 20005
int n,m,x,y,l=1,ans,cnt;
int son[N],ed[N],next[N],d[N],c[N],f[N],o[N],pre[N];
bool b[N];
void dfs(int x,int fa)
{
	b[x]=1;
	for (int p=son[x];p;p=next[p]){
		int y=ed[p]; if (y==fa || d[y]>d[x]) continue;
		if (!b[y]) d[y]=d[x]+1,dfs(y,x),c[p]=f[y],f[x]+=f[y];
		else if ((d[x]&1)==(d[y]&1)) f[x]++,f[y]--,c[p]++,cnt++;
			else f[x]--,f[y]++;
		}
}
int main()
{
	scanf("%d%d",&n,&m);
	for (int i=1;i<=m;i++) scanf("%d%d",&x,&y),
		ed[++l]=y,next[l]=son[x],son[x]=l,
		ed[++l]=x,next[l]=son[y],son[y]=l;
	for (int i=1;i<=n;i++) if (!b[i]) dfs(i,0); if (cnt>1) ans=0;
	if (!cnt) for (int i=1;i<=m;i++) o[ans++]=i;
	else for (int i=2;i<=m+m+1;i++) if (c[i]==cnt) o[ans++]=i/2;
	printf("%d\n",ans);
	for (int i=0;i<ans;i++) printf("%d%s",o[i],i<ans-1?" ":"\n");
	return 0;
}