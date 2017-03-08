#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
#define N 100050
#define M 2000050
#define INF 0x7f7f7f7f
struct Edge {int u,v,w,sg,use;} a[M],b[N];
int n,m,len,ans,Rt,pre[N],sg[N],mi[N],li[N],vis[N];
inline int Read()
 {
    int x=0;char y;
    do y=getchar(); while (y<'0'||y>'9');
    do x=x*10+y-'0',y=getchar(); while (y>='0'&&y<='9');
    return x;
 }
int solve()
 {
    for (int i=1;i<=n;i++)
      pre[i]=sg[i]=li[i]=vis[i]=0,mi[i]=INF;
    for (int i=1;i<=m;i++)
     if (b[i].u!=b[i].v&&b[i].w<mi[b[i].v])
       pre[b[i].v]=b[i].u,mi[b[i].v]=b[i].w,li[b[i].v]=b[i].sg;
    for (int i=1;i<=n;i++)
     if (i!=Rt&&!pre[i]) return 0;
    int cnt=0;mi[Rt]=0;
    for (int i=1;i<=n;i++)
     {
        if (i!=Rt) a[li[i]].use++;
        int now=i;ans+=mi[i];
        while (!vis[now]&&now!=Rt)
          vis[now]=i,now=pre[now];
        if (now!=Rt&&vis[now]==i)
         {
            cnt++;int k=now;
            while (1)
             {
                sg[now]=cnt;now=pre[now];
                if (sg[now]==cnt) break;
             }
         }
     }
    if (!cnt) return 1;
    for (int i=1;i<=n;i++)
     if (!sg[i]) sg[i]=++cnt;
    for (int i=1;i<=m;i++)
     {
        int k=mi[b[i].v],l=b[i].v;
        b[i].u=sg[b[i].u],b[i].v=sg[b[i].v];
        if (b[i].u!=b[i].v)
          b[i].w-=k,a[++len].u=b[i].sg,a[len].v=li[l],
          b[i].sg=len;
     }
    n=cnt;Rt=sg[Rt];
    return 2;
 }
bool Solve()
 {int Ans;while ((Ans=solve())==2);return Ans;}
int main()
 {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    n=Read();m=len=Read();Rt=1;
    for (int i=1;i<=m;i++)
      b[i].sg=i,b[i].u=Read(),b[i].v=Read(),
      b[i].w=a[i].w=Read();
    if (!Solve()) {puts("-1");return 0;}
    cout <<ans<<endl;
    for (;len>m;len--)
      a[a[len].u].use+=a[len].use,a[a[len].v].use-=a[len].use;
    for (int i=1;i<=m;i++)
     if (a[i].w&&a[i].use) printf("%d ",i);
    puts("");
    return 0;
 }