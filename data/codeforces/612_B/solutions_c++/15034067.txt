#include <iostream>
#include <cmath>
using namespace std;
int v[201010],n,i,x;
long long s;
int main()
{
    cin>>n;
    for(i=1;i<=n;i++)
    cin>>x,v[x]=i;
    for(i=1;i<n;i++)
        s+=abs(v[i+1]-v[i]);
    cout<<s;
}
