#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
#define sqr(x) ((x)*(x))

struct GOAL{ double x,y,t,p; } a[1010];
int n;
double f[1010],ans;

bool cmp(GOAL a,GOAL b) { return a.t<b.t; }

int main()
{
    scanf("%d",&n);
    for (int i=1;i<=n;i++) scanf("%lf%lf%lf%lf",&a[i].x,&a[i].y,&a[i].t,&a[i].p);
    sort(&a[1],&a[n+1],cmp);
    for (int i=1;i<=n;i++)
    {
        f[i]=a[i].p;
        for (int j=1;j<i;j++)
        {
            if (sqr(a[i].t-a[j].t)-sqr(a[i].x-a[j].x)-sqr(a[i].y-a[j].y)>-1e-7) 
                f[i]=max(f[j]+a[i].p,f[i]);
        }
        ans=max(ans,f[i]);
    }
    printf("%.7f\n",ans);
    
    return 0;
}