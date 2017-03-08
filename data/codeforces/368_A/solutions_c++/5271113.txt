#include<bits/stdc++.h>
using namespace std;
int n,d;
int m,a[1000],ans;
int main()
{
    cin>>n>>d;
    for(int i=1;i<=n;i++)cin>>a[i];
    sort(a+1,a+n+1);//reverse(a+1,a+n+1);
    cin>>m;
    for(int i=1;i<=min(n,m);i++)ans+=a[i];
    for(int i=1;i<=m-n;i++)ans-=d;
    cout<<ans<<endl;
}
