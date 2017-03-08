#include <bits/stdc++.h>

using namespace std;

long long n,a[200005],i,s,x;

int main()
{
    cin>>n;
    for (i=1;i<=n;++i) {
        cin>>x;
        a[x]=i;
    }
    for (i=1;i<n;++i)
        s+=abs(a[i]-a[i+1]);

    cout<<s;
    return 0;
}
