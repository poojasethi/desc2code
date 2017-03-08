#include<cstdio>
#include<cstring>
const int N=505,M=130005;
int n,m,Q,l=1,S,T,x,y,z,a[N][N],d[N],pre[N],f[M*5],c[M];
int st[M],ed[M],data[M],cost[M],next[M],son[N];
bool b[N];
void addedge(int x,int y,int z,int c)
{
	st[++l]=x; ed[l]=y; data[l]=z; cost[l]=c; next[l]=son[x]; son[x]=l;
	st[++l]=y; ed[l]=x; data[l]=0; cost[l]=-c; next[l]=son[y]; son[y]=l;
}
int spfa()
{
	for (int i=S;i<=T;i++) d[i]=100000000,b[i]=0;
	int h=0,t=1; f[1]=S; d[S]=0;
	while (h<t){
		int i=f[++h]; b[i]=0; if (d[i]>=d[T]) continue;
		for (int p=son[i];p;p=next[p]) if (data[p]){
			int j=ed[p]; if (d[i]+cost[p]>=d[j]) continue;
			d[j]=d[i]+cost[p]; pre[j]=p; if (!b[j]) b[j]=1,f[++t]=j;
			}
		}
	for (int p=T;p!=S;p=st[p]) p=pre[p],data[p]--,data[p^1]++;
	return d[T];
}
int main()
{
	scanf("%d%d%d",&n,&m,&Q); S=0; T=n+n+1; memset(a,6,sizeof(a));
	for (int i=1;i<=m;i++) scanf("%d%d%d",&x,&y,&z),a[x][y]=a[x][y]<z?a[x][y]:z;
	for (int i=1;i<=n;i++)
		for (int j=1;j<=n;j++)
			for (int k=1;k<=n;k++)
				if (a[i][k]+a[k][j]<a[i][j]) a[i][j]=a[i][k]+a[k][j];
	for (int i=1;i<=n;i++) addedge(S,i,1,0),addedge(i+n,T,1,0);
	for (int i=1;i<=n;i++) for (int j=1;j<=n;j++) addedge(i,j+n,1,a[i][j]);
	int now=spfa(),cnt=n;
	for (int i=0;i<=10000;i++){
		while (now==i) cnt--,now=spfa();
		c[i+1]=c[i]+cnt;
		}
	while (Q--) scanf("%d",&x),printf("%d\n",c[x]);
	return 0;
}
