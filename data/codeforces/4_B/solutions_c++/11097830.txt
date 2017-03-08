#include<iostream>
using namespace std;
int n,m,i,a[100],b[100],k,x;
int main(){
cin>>n>>m;
for(i=0;i<n;i++)
{
cin>>a[i]>>b[i];
k+=a[i];
x+=b[i];
}
if(m<k || m>x)
{
cout<<"NO";
return 0;
}
cout<<"YES"<<endl;
for(i=0;i<n;i++){
cout<<min(b[i],m-k+a[i])<<" ";
m-=min(b[i],m-k+a[i]);
k-=a[i];
}
}