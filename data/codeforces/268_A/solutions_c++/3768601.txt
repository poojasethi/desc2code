#include<iostream>
using namespace std;
int main()
{
int n,i,j,s;
cin>>n;
int ar[n][2];
for(i=0;i<n;i++)
cin>>ar[i][0]>>ar[i][1];
s=0;
for(i=0;i<n;i++)
for(j=0;j<n;j++)
if(ar[i][1]==ar[j][0])
s++;
cout<<s;
return 0;
}