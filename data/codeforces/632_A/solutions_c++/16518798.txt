#include<bits/stdc++.h>
using namespace std;
#define ll long long int
string s[45];
int main(){
    ll n,p,k,ans;
    cin>>n>>p;
    for(ll i=1;i<=n;i++){
        cin>>s[i];
    }

    k=0,ans=0;
    for(ll i=n;i>=1;i--){
        k*=2;
        if(s[i]=="halfplus") k++;
        ans+=(k*p)/2;
    }

    cout<<ans<<endl;
}
