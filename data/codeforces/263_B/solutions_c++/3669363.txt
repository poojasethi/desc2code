#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
int n,k;
scanf("%d%d",&n,&k);
int i,j,a[7777];

for(i=0;i<n;i++)
scanf("%d",&a[i]);
sort(a,a+n);
if(k>n)printf("-1");
else printf("%d 0",a[n-k]);
return 0;
}