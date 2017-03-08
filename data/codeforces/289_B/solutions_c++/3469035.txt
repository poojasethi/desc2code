#include<stdio.h>
#include<algorithm>
#include<iostream>
using namespace std;
int a[10001];
int main()
{
    int n,k,i,m,t,ans=0;
    scanf("%d%d%d",&n,&m,&k);
    n*=m;
    for(i=0; i<n; i++)
    scanf("%d",&a[i]);
    sort(a,a+n);
    t=n/2;
    for(i=0; i<n; i++)
      if( ( abs(a[t]-a[i]) )%k==0) ans+=( abs(a[t]-a[i]) )/k;
        else { printf("-1\n"); return 0; }   
    printf("%d\n",ans);
}