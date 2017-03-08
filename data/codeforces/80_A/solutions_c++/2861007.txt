#include<iostream>
using namespace std;
int main()
{
int a[]={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,51};
int i,n,m;
cin>>n>>m;
for(i=0;a[i]!=n;i++);
if(a[i+1]==m)
cout<<"YES";
else
cout<<"NO";
}