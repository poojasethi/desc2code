#include<bits/stdc++.h>
using namespace std;
int n,m,a,b,mxa,mna=999999,mnb=999999;
int main()
{
    cin>>n>>m;
    for(int i=1;i<=n;i++)cin>>a,mxa=max(a,mxa),mna=min(mna,a);
    for(int i=1;i<=m;i++)cin>>b,mnb=min(b,mnb);
    if(max(2*mna,mxa)<mnb)cout<<max(2*mna,mxa)<<endl;
    else cout<<-1<<endl;
}
