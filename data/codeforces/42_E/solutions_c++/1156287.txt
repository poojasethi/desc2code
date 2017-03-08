#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
typedef long long LL;
const int MAXN = 100010;
const int MAXM = 200010;
struct Edge
{
    int u,v,len,pre;
};
Edge e[MAXM],e2[MAXM];
int hh[MAXN],e_cnt;
void addEdge(int u,int v,int len)
{
    e[e_cnt].u=u;
    e[e_cnt].v=v;
    e[e_cnt].len=len;
    e[e_cnt].pre=hh[u];
    hh[u]=e_cnt++;
}
bool cmp(const Edge &a1,const Edge &a2)
{
    return a1.len<a2.len;
}
int vis[MAXN],dep[MAXN],pre[MAXN][20],len[MAXN][20];
int fa[MAXN];
int find(int x)
{
    if (fa[x]==x) return x;
    return fa[x]=find(fa[x]);
}
void dfs(int u,int d)
{
    vis[u]=1;
    dep[u]=d;
    int fa;
    if (d==0)
    {
        fa=u;
        len[u][0]=0;
    }
    else fa=pre[u][0];
    for (int i=1;i<=16;i++)
    {
        pre[u][i]=pre[pre[u][i-1]][i-1];
        len[u][i]=max(len[u][i-1],len[pre[u][i-1]][i-1]);
    }
    for (int i=hh[u];i!=-1;i=e[i].pre)
    {
        int v=e[i].v;
        if (!vis[v])
        {
            pre[v][0]=u;
            len[v][0]=e[i].len;
            dfs(v,d+1);
        }
    }
}
int query(int u,int v)
{
    int ans=0;
    if (dep[u]>dep[v]) swap(u,v);
    int num=dep[v]-dep[u],cnt=0;
    while (num!=0)
    {
        if (num%2==1)
        {
            ans=max(ans,len[v][cnt]);
            v=pre[v][cnt];
        }
        cnt++;
        num/=2;
    }
    if (u==v) return ans;
    for (int i=16;i>=0;i--)
    {
        if (pre[u][i]!=pre[v][i])
        {
            ans=max(ans,len[u][i]);
            ans=max(ans,len[v][i]);
            u=pre[u][i];
            v=pre[v][i];
        }
    }
    ans=max(ans,len[u][0]);
    ans=max(ans,len[v][0]);
    return ans;
}
int main()
{
    int n;
    while (scanf("%d",&n)==1)
    {
        int m;
        scanf("%d",&m);
        memset(hh,-1,sizeof(hh));
        for (int i=0;i<m;i++)
            scanf("%d%d%d",&e2[i].u,&e2[i].v,&e2[i].len);
        sort(e2,e2+m,cmp);
        for (int i=1;i<=n;i++)
            fa[i]=i;
        e_cnt=0;
        LL sum=0;
        for (int i=0;i<m;i++)
        {
            if (find(e2[i].u)!=find(e2[i].v))
            {
                fa[find(e2[i].u)]=find(e2[i].v);
                addEdge(e2[i].u,e2[i].v,e2[i].len);
                addEdge(e2[i].v,e2[i].u,e2[i].len);
                sum+=e2[i].len;
            }
        }
        memset(vis,0,sizeof(vis));
        int c_cnt=0;
        for (int i=1;i<=n;i++)
        {
            if (!vis[i])
            {
                c_cnt++;
                dfs(i,0);
            }
        }
        int q;
        scanf("%d",&q);
        while (q--)
        {
            int u,v;
            scanf("%d%d",&u,&v);
            if (c_cnt>2) puts("-1");
            else if (c_cnt==2)
            {
                if (find(u)==find(v)) puts("-1");
                else printf("%I64d\n",sum);
            }
            else
                printf("%I64d\n",sum-query(u,v));
        }
    }
    return 0;
}
