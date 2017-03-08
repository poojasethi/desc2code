#include<bits/stdc++.h>
using namespace std;
main()
{
long long n,m,arr[40000],i,f=0;
cin>>n>>m;
for(i=0;i<m;i++)
cin>>arr[i];
sort(arr,arr+m);
if(arr[0]==1||arr[m-1]==n)cout<<"NO"<<endl;
else
{

for(i=0;i<m-2;i++)
{
if(arr[i]==(arr[i+1]-1)&&arr[i]==(arr[i+2]-2))
{
    f=1;
    break;
}
}
if(f)cout<<"NO"<<endl;
else cout<<"YES"<<endl;
}
}
