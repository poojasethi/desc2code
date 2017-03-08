#include<iostream>
using namespace std;
int main(){
int n,d=1;
cin>>n;
for(int i=0;i<n-1;i++)
d+=i,d%=n,d++,cout<<d<<" ";
}