#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>
#include<cmath>
#define ll long long
using namespace std;
const ll maxn= 5e3;
struct node{
	ll a,b;
	bool operator <(const node &x)const{
		return a<x.a;
	};
}a[maxn];
ll b[maxn];
ll n,i,j,k,ans,la,x,y,z;
int main()
{
	//freopen("1.in","r",stdin);
	//freopen("1.out","w",stdout);
	scanf("%lld",&n);
	for (i= 1;i<=n;i++){
		scanf("%lld%lld",&a[i].a, &a[i].b);
		if (a[i].a>a[i].b) swap(a[i].a,a[i].b);
	}
	sort(a+1,a+n+1);
	for (i= n;i>=1;i--){
		b[++la]= a[i].b;
		sort(b+1,b+la+1);
		for (j= la;j>=1;j--){
			z= a[i].a*b[j]*(la-j+1);
			if (ans<z){
				ans= z;
				x= a[i].a;
				y= b[j];
			}
		}
	}
	printf("%lld\n%lld %lld\n",ans, x, y);
	return 0;
}
