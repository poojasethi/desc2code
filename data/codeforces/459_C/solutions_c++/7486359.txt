#include<iostream>
using namespace std;
int main()
{
long int k,d,i,n,b=1;
cin>>n>>k>>d;
for(i=0; i<d; i++)
{
b*=k;
if(b>n)
break;
}
if(i==d && b<n)
{
cout<<"-1";
return 0;
}
b/=k;
for(d; d>0; d--)
if(b>0)
{
for(i=0; i<n; i++)
cout<<(i/b)%k+1<<' ';
cout<<'\n';
b/=k;
}
else
{
for(i=0; i<n; i++)
cout<<"1 ";
cout<<'\n';
}
return 0;
}