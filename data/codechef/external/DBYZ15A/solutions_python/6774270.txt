#include <bits/stdc++.h>
#define ll long long
using namespace std;
ll a[1000006];
int main()
{
    ios_base::sync_with_stdio(false);
    ll n,i,x;
    cin>>n;
    for(i=0;i<n;i++)
    {
        cin>>x;
        a[x]++;
    }
    ll res = (n*(n-1))/2;
    for(i=0;i<1000006;i++)
    {
        res = res - (a[i]*(a[i]-1))/2;
    }
    printf("%lld\n",res);
    return 0;
}
