#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define afor(i,N) for(i;i<N;i++)
#define beg ll T;cin>>T;while(T--)

int main(){
beg{
    ll N,n;
    cin>>N;
    vector<ll> v;
    v.clear();
    ll i=0;
    afor(i,N){
        cin>>n;
        v.push_back(n);
    }
    i=0;
    ll cost=0,min1=v[0];
    for(i=1;i<N;i++){
           if(min1>v[i]){
                min1=v[i];
           }
    }
    cout<<min1*(N-1)<<endl;
}
return 0;
}
