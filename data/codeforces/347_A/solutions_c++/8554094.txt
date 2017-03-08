#include<bits/stdc++.h>
using namespace std;
int n,a[200],i;
int main()
{
    cin>>n;
    for(i=1;i<=n;i++) cin>>a[i];
    sort(a+1,a+n+1);
    swap(a[1],a[n]);
    for(i=1;i<=n;i++) cout<<a[i]<<" ";
    return 0;
}
