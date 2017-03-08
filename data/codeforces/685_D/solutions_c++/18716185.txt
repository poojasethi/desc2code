#include<cstdio>
#include<cmath>
#include<stdlib.h>
#include<map>
#include<set>
#include<time.h>
#include<vector>
#include<stack>
#include<queue>
#include<string>
#include<string.h>
#include<iostream>
#include<algorithm>
using namespace std;
#define eps 1e-8
const int maxn=100005;
struct event
{
    long long l,r,y,v;
    event(){}
    event(long long L,long long R,long long Y,long long V)
    {
        l=L;
        r=R;
        y=Y;
        v=V;
    }
    bool operator < (const event &x)const
    {
        return y<x.y;
    }
};
long long ans[maxn];
long long x[maxn*2];
int cnt[maxn*2];
event E[maxn*2];
int n,k;
long long last[maxn*2];
const long long inf=(1LL<<40);
int main()
{
    scanf("%d%d",&n,&k);
    int tot=0;
    x[tot++]=-inf;
    for(int i=0;i<n;i++)
    {
        long long X,Y;
        scanf("%I64d%I64d",&X,&Y);
        x[tot++]=X;
        x[tot++]=X+k;
        E[2*i]=event(X,X+k,Y,1);
        E[2*i+1]=event(X,X+k,Y+k,-1);
    }
    sort(x,x+tot);
    tot=unique(x,x+tot)-x;
    sort(E,E+2*n);
    for(int i=0;i<tot;i++)
        last[i]=-inf;
    for(int i=0;i<2*n;i++)
    {
        int l=upper_bound(x,x+tot,E[i].l)-x;
        int r=lower_bound(x,x+tot,E[i].r)-x;
        for(int j=l;j<=r;j++)
        {
            ans[cnt[j]]+=(x[j]-x[j-1])*(E[i].y-last[j]);
            cnt[j]+=E[i].v;
            last[j]=E[i].y;
        }
    }
    for(int i=1;i<=n;i++)
        printf("%I64d ",ans[i]);
    return 0;
}
