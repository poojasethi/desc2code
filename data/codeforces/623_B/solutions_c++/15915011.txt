#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>
#include<cmath>
#define ll long long
using namespace std;
const ll oo= 1e18;
const ll maxn= 1e6+10;
ll a[maxn],f[maxn][4];
ll ans;
ll n,A,B,i,j;
bool ok(ll x,ll y){
	return x%y==0;
}
void go(ll r){
	ll i,j;
	f[0][0]= 0;
	f[0][1]= oo;
	f[0][2]= oo;
	for (i= 1;i<=n;i++){
		for (j= 0;j<=2;j++)
			f[i][j]= oo;
		//0
		if (ok(a[i],r)) f[i][0]= f[i-1][0];
		else if (ok(a[i]-1,r)||ok(a[i]+1,r))
			f[i][0]= f[i-1][0]+B;

		//1
		f[i][1]= min(f[i-1][0],f[i-1][1])+A;
		
		//2
		ll x= min(f[i-1][1],f[i-1][2]);
		if (ok(a[i],r)) f[i][2]= x;
		else if (ok(a[i]-1,r)||ok(a[i]+1,r))
			f[i][2]= x+B;
		
		//2
	}
	for (i= 0;i<=2;i++)
		ans= min(ans,f[n][i]);
}
void start(ll x){
	for (ll i= 2;i*i<=x;i++)
		if (x%i==0){
			go(i);
			while (x%i==0) x/= i;
		}
	if (x!=1) go(x);
}
int main()
{
	//freopen("1.in","r",stdin);
	//freopen("1.out","w",stdout);
	ans= oo;
	scanf("%lld%lld%lld",&n, &A, &B);
	for (i= 1;i<=n;i++)
		scanf("%lld",&a[i]);
	start(a[1]-1);
	start(a[1]);
	start(a[1]+1);
	reverse(a+1,a+n+1);
	start(a[1]-1);
	start(a[1]);
	start(a[1]+1);
	printf("%lld\n",ans);
	return 0;
}
