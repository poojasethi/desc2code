#include<bits/stdc++.h>
using namespace std;
int i=1,k=1,n,m,a[200],b[200],ans;
int main()
{
    cin>>n>>m;
    while(n--) cin>>a[i++];
    while(m--) cin>>b[k++];
    sort(a+1,a+i);
    sort(b+1,b+k);
    ans=a[i-1];
    ans=max(a[1]*2,a[i-1]);
    if(b[1]>ans)
        cout<<ans<<endl;
    else cout<<-1<<endl;
}
