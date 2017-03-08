#include<stdio.h>
#include<math.h>
#include<algorithm>
using namespace std;
const int maxn=100050,maxq=5050,INF=0x7fffffff;
struct Seg
{
    int l,r;
    double p;
    Seg() {}
    Seg(int l,int r,double p):l(l),r(r),p(p) {}
    bool operator < (const Seg &yy) const { return l!=yy.l?l<yy.l:r>yy.r; }
    void scan() { scanf("%d%d%lf",&l,&r,&p); }
};
int n,q,a[maxn];
Seg op[maxq];
double ans=0;
int minf[maxq];
double f[maxq][maxq];
bool vis[maxq];
int cov[maxq],son[maxq][maxq],ss[maxq];
void DP(int x)
{
    vis[x]=1;
    int i,j,y;
    for(i=x+1;i<q&&op[i].r<=op[x].r;i++)
        if(!vis[i])
            DP(son[x][ss[x]++]=i),cov[x]=max(cov[x],cov[i]);
    for(i=0,j=op[x].l;i<ss[x];i++)
    {
        while(j<op[son[x][i]].l)
            minf[x]=max(minf[x],a[j++]);
        minf[x]=max(minf[x],minf[son[x][i]]);
        j=op[son[x][i]].r+1;
    }
    while(j<=op[x].r) minf[x]=max(minf[x],a[j++]);
    //printf("%d   %d %d  %d\n",x,op[x].l,op[x].r,minf[x]);
    f[x][0]=1;
    for(i=1;i<=cov[x];i++)
    {
        double t=0,t1=1,t2=1;
        f[x][i]=1;
        for(j=0;j<ss[x];j++)
        {
            y=son[x][j];
            int tt=minf[x]+i-minf[y];
            if(tt<=cov[y])
            {
                t1*=f[y][tt];
                t2*=!tt?0:f[y][tt-1];
            }
        }
        f[x][0]-=(f[x][i]=t1-t2);
    }
    cov[x]++;
    for(i=cov[x];i;i--)
        f[x][i]=f[x][i-1]*op[x].p+f[x][i]*(1-op[x].p);
    f[x][0]=f[x][0]*(1-op[x].p);
    //for(i=0;i<=cov[x];i++) printf("%.2lf ",f[x][i]); printf("\n");
    for(i=1;i<=cov[x];i++)
        f[x][i]=f[x][i]+f[x][i-1];
}
int main()
{
#ifndef ONLINE_JUDGE
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
#endif
    int i,j;
    scanf("%d%d",&n,&q);
    for(i=1;i<=n;i++)
        scanf("%d",&a[i]);
    for(i=0;i<q;i++)
        op[i].scan();
    op[q++]=Seg(1,n,0);
    sort(op,op+q);
    DP(0);
    ans=minf[0]*f[0][0];
    for(i=1;i<=cov[0];i++)
        ans+=(minf[0]+i)*(f[0][i]-f[0][i-1]);
    printf("%.8lf\n",ans);
    return 0;
}