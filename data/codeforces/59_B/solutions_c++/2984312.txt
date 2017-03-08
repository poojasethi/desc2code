#include<iostream>
using namespace std;
int n,a,s,m=1e9;
int main()
{
    cin>>n;
    while(n--)
        cin>>a,s+=a,a%2?m=min(m,a):0;
    cout<<(s%2?s:max(0,s-m));
}