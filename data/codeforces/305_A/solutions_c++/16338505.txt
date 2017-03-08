#include<iostream>
using namespace std;
int main()
{
int k,y=0,n=0,x,i,f=0,f1=0,ans[111];
cin>>k;
for (i=1; i<=k; i++)
{
cin>>x;
if (x==0 || x==100) ans[++n]=x; else 
if (x<10 && !f) ans[++n]=x,f=1; else
if (x%10==0 && !f1) ans[++n]=x,f1=1; else y=x;
}
if (!f && !f1 && y) ans[++n]=y;
cout<<n<<endl;
for (i=1; i<=n; i++)
cout<<ans[i]<<" ";
return 0;
}