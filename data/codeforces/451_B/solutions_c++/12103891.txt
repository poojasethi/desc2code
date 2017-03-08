#include <bits/stdc++.h>
using namespace std;
int main(){
int n,i;
cin>>n;
int arr[n],b[n];
for(i=0;i<n;i++){
cin>>arr[i];
b[i]=arr[i];
}
sort(arr,arr+n);
int marker=0,f=-1,s=0;
for(i=0;i<n;i++){
if(arr[i]!=b[i]){if(f==-1)f=i;s=i;}
}
int j;
if(f==-1)f=0;
if(s==0)s=0;
for(i=f,j=s;i<=s;i++,j--)if(arr[i]!=b[j])
{cout<<"no\n";return 0;}
cout<<"yes\n"<<f+1<<" "<<s+1<<"\n";
return 0;
}
