#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<vector>
#include<map>
#define ll long long
using namespace std;
const ll maxn= 3e3;
struct node{
	ll x,y;
};
map<ll,node> M;
map<ll,node> ::iterator it;
ll a[maxn],b[maxn];
ll X[10],Y[10];
ll n,m,sa,sb,v,k,i,j,x;
void read(ll &n,ll &sa,ll *a){
	scanf("%I64d",&n);
	for (ll i= 1;i<=n;i++){
		scanf("%I64d",&a[i]);
		sa+= a[i];
	}
}
void update(ll x,ll i,ll j,map<ll,node> ::iterator it){
	if (abs(x-it->first)<v){
		v= abs(x-it->first);
		k= 2;
		X[1]= it->second.x;
		Y[1]= i;
		X[2]= it->second.y;
		Y[2]= j;
	}	
}
int main()
{
	//freopen("1.in","r",stdin);
	//freopen("1.out","w",stdout);
	read(n,sa,a);
	read(m,sb,b);
	v= abs(sa-sb);
	k= 0;	
	for (i= 1;i<=n;i++)
		for (j= 1;j<=m;j++){
			x= abs(sa-sb-2*a[i]+2*b[j]);
			if (x<v){
				v= x;
				X[k= 1]= i;
				Y[1]= j;
			}
		}
	for (i= 1;i<=n;i++)
		for (j= i+1;j<=n;j++)
			M[2*(a[i]+a[j])]= (node){i,j};
	if (!M.empty()){
		for (i= 1;i<=m;i++)
			for (j= i+1;j<=m;j++){
				x= sa-sb+2*(b[i]+b[j]);
				it= M.lower_bound(x);
				update(x,i,j,it);
				if (it!=M.begin()){
					it--;
					update(x,i,j,it);
				}
			}
	}
	printf("%I64d\n%I64d\n",v, k);
	for (i= 1;i<=k;i++)
		printf("%I64d %I64d\n",X[i], Y[i]);
	return 0;
}
