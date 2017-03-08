#include<bits/stdc++.h>
using namespace std;
int a[200],n,i;
int main()
{
    cin>>n;
    for(i=1;i<=n;i++)
        cin>>a[i];
    for(i=2;i<=n;i++)
    a[i]=__gcd(a[i-1],a[i]);
    cout<<n*a[n]<<endl;

}
