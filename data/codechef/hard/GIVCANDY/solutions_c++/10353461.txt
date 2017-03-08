#include<bits/stdc++.h>

using namespace std;

#define fin freopen("i1.txt","r",stdin)
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define fastio ios_base::sync_with_stdio(false); cin.tie(0);
#define ll long long
#define oo(x) do{ for(int zo=1;zo<=5;zo++) cout<<x; cout<<"\n"; }while(0);

int main(){

    ll t;
    cin>>t;

    while(t--){
        ll a,b,c,d;
        cin>>a>>b>>c>>d;

        ll g=__gcd(c,d);

        cout<<min( ((a-b)%g+g)%g , ((b-a+g)%g+g)%g  )<<endl;
    }

    return 0;
}
