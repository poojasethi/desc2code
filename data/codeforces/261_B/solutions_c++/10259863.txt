#include <iostream>
#include <cstdio>
#define LMT 55
//先把总的情况的个数算出来，然后再除以总情况
using namespace std;
double dp[LMT][LMT];
int n,p,a[LMT];
double fi[LMT];
void init()
{
    fi[0]=1.0;
    for(int i=1;i<LMT;i++)fi[i]=i*fi[i-1];
}
int main()
{
    init();
    double ans=0;
    dp[0][0]=1;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)scanf("%d",&a[i]);
    scanf("%d",&p);
    for(int i=1;i<=n;i++)
        for(int j=n;j>=1;j--)
           for(int t=p;t>=a[i];t--)
               dp[j][t]+=dp[j-1][t-a[i]];
    for(int i=1;i<=n;i++)//定下两半的位置
      for(int j=1;j<=p;j++)
        ans+=dp[i][j]*fi[i]*fi[n-i];
    printf("%.6lf\n",ans/fi[n]);
    return 0;
}