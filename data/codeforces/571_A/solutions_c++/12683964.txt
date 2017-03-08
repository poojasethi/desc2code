#include<bits/stdc++.h>
#define ll long long
using namespace std;
ll ans;
ll gao(ll a,ll b,ll c,ll m){
    ll cnt=min(a-b-c,m);
    if(cnt<0)return 0;
    return (cnt+1)*(cnt+2)/2;
}
int main()
{
    ll a,b,c,l;
    cin>>a>>b>>c>>l;
    ans+=(l+3)*(l+2)*(l+1)/6;
    for(ll i=0;i<=l;i++)
        ans-=gao(a+i,b,c,l-i)+gao(b+i,a,c,l-i)+gao(c+i,a,b,l-i);
    cout<<ans;
}
