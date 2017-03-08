#include<bits/stdc++.h>
using namespace std;
#define ll long long int

ll bin_src(ll x){
    ll ans=0;
    for(ll i=2;i*i*i<=x;i++){
        ans+=x/(i*i*i);
    }

    return ans;
}

int main(){
    ll m,n=-1;
    cin>>m;
    ll l=1,h=9e15;
    while(l<h){
        ll mid=(l+h)>>1;
        if(bin_src(mid)<m) l=mid+1;
        else h=mid;
    }

    if(bin_src(l)==m) n=l;
    cout<<n<<"\n";
    return 0;
}
