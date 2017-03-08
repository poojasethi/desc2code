#include<iostream>
using namespace std;
int n,k;
int main()
{
    cin>>n>>k;
    for(int i=n;i>=n-k+1;i--)cout<<i<<" ";
    for(int i=1;i<=n-k;i++)cout<<i<<" ";
    cout<<endl;
}
