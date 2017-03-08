#include<bits/stdc++.h>
#include<algorithm>
const int P=(int)1e6+3;
using namespace std;
typedef long long ll;
ll n,m;
ll qpow(ll a,ll b){ll ans=1;for(ll i=b;i;i>>=1,a=(a*a)%P)if(i&1)ans=ans*a%P;return ans;}
ll C(ll a,ll b){
	if(b>a)return 0;if(b>a-b)b=a-b;
	ll s1=1,s2=1;
	for(ll i=1;i<=b;i++)
	{
		s1=s1*(a-i+1)%P;
		s2=s2*i%P;
	}
	return s1*qpow(s2,P-2)%P;
} 

ll lucas(ll a,ll b){return C(a/P,b/P)*C(a%P,b%P);}
int main(){
	ios::sync_with_stdio(0);
	cin>>n>>m;cout<<(lucas(n+m,min(n,m))-1+P)%P;
	return 0;
}