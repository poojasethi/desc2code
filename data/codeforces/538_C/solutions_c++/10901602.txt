#include<bits/stdc++.h>
#define ll long long
using namespace std;
ll h[100001],d[100001],ans;
int main()
{
    int i,n,m;
    cin>>n>>m;
    for(i=1;i<=m;i++) scanf("%d%d",h+i,d+i);
    ans=max(h[1]+d[1]-1,d[m]+n-h[m]);
    for(i=2;i<=m;i++){
        if(h[i]-h[i-1]<abs(d[i]-d[i-1])) return puts("IMPOSSIBLE");
        ans=max((h[i]-h[i-1]+d[i]+d[i-1])/2,ans);
    }
    cout<<ans<<endl;
}
