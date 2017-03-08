#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;
typedef long long ll;

const int N = 22;

ll mod = 1e9+7;

ll inv[N], a[N];

ll Cnk(ll n, int k){
	if(n<k) return 0;
	ll r = 1;
	for(ll x = n-k+1; x<=n; ++x) r = x%mod*r%mod;
	for(int i=1;i<=k;++i) r = r*inv[i]%mod;
	return r;
}

int main(){
       int n;
    ll s, sum = 0;;
    
    
    inv[1]=1;
    for(int i=2;i<20;++i) inv[i] = (mod-mod/i)*inv[mod%i]%mod;
    
    cin>>n>>s;
    for(int i=0;i<n;++i){
    	cin>>a[i];
    	sum+=a[i];
    }
    
    ll ans = 0;
    for(int ms = 0;ms<1<<n;++ms){
    	ll z = s, l = 1;
    	for(int i=0;i<n;++i) if(ms>>i&1){
    		l = -l;
    		z-=a[i]+1;
    	}
	
		ans+=l*Cnk(z+n-1,n-1);
    	ans%=mod;
    	ans+=mod;
    	ans%=mod;
    }
    
    cout<<ans<<endl;
   
}
