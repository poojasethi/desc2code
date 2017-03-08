#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>
#include<cmath>
#define ll long long
using namespace std;
const ll maxn= 2e5;
pair<ll,ll> a[maxn];
ll sum[maxn],b[maxn];
ll n,A,cf,cm,m,i,j,k,ans,p,xx,yy,x;
int main()
{
	//freopen("1.in","r",stdin);
	//freopen("1.out","w",stdout);
	scanf("%lld%lld%lld%lld%lld",&n, &A, &cf, &cm, &m);
	for (i= 1;i<=n;i++){
		scanf("%lld",&a[i].first);
		a[i].second= i;
	}
	sort(a+1,a+n+1);
	for (i= 1;i<=n;i++)
		sum[i]= sum[i-1]+a[i].first;
	p= n;
	for (i= 0;i<=n;i++){
		ll d= m-(A*i-(sum[n]-sum[n-i]));
		if (d<0) break;
		p= min(p,n-i);
		if (p==0){
			x= cf*i+cm*A;
			k= A;
		}else {
			while(d<a[p].first*(p-1)-sum[p-1]) p--;
			d-= a[p].first*(p-1)-sum[p-1];
			k= min(a[p].first+d/p,A);
			x= cf*i+cm*k;
		}
		if (ans<x){
			ans= x;
			xx= i;
			yy= k;
		}
	}
	printf("%lld\n",ans);
	for (i= n-xx+1;i<=n;i++)
		b[a[i].second]= A;
	for (i= 1;i<=n-xx;i++)
		b[a[i].second]= max(a[i].first,yy);
	for (i= 1;i<=n;i++)
		printf("%lld%c",b[i], i<n?' ':'\n');
	return 0;
}
