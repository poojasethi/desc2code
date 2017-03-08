#include <bits/stdc++.h>
using namespace std;
#define N 200005
int a[N];
int main()
{
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
        scanf("%d",&a[i]);
    sort(a,a+n);
    int ans  = 1e9;
    for(int i=0;i<n/2;i++)
        ans = min(ans , a[i+n/2] - a[i]);
    cout<<ans;
    return 0;
}