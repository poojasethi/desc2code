#include<bits/stdc++.h>
using namespace std;

int main()
{
    int c1,c2,c3,c4,c=0,i,m,n,ans=0,t;
    cin>>c1>>c2>>c3>>c4;
    cin>>n>>m;
    for(i=1;i<=n;i++)
    {
        cin>>t;
        c+=min(c1*t,c2);
    }
    ans+=min(c,c3);
    c=0;
    for(i=1;i<=m;i++)
    {
        cin>>t;
      c+= min(t*c1,c2);
    }
    ans+=min(c,c3);
    ans=min(ans,c4);
    cout<<ans<<endl;
    return 0;
}
