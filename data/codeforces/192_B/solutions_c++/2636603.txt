#include<iostream>
using namespace std;
int main()
{
int n,a[1005],b[1005],i;
cin>>n;
b[0]=1000000;
for(i=1;i<=n;i++)
{
cin>>a[i];
b[i]=b[i-1];
if(i>2 && b[i-2]>b[i]) b[i]=b[i-2];
b[i]=min(a[i],b[i]);
}
cout<<b[n];
return 0;
}