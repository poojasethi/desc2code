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
const ll maxn= 3e5;
char s[maxn],S[10];
ll day[maxn];
ll sum[200][30],d[200][30];
ll len,i,j,n,m,mx,ans;
ll dfs(ll x,ll mx,ll c){
	if (!mx) return sum[x][c];
	if ((len<<(mx-1))>x) return dfs(x,mx-1,c);
	else if ((len<<(mx-1))==x) return sum[len][c]<<(mx-1);
	else {
		ll ans= 0;
		if ((len<<(mx-1))+day[mx]<=x){
			ans= (sum[len][c]<<(mx-1))+d[mx][c];
			ans+= dfs(x-(len<<(mx-1))-day[mx],mx-1,c);
		}else 
			ans= d[mx][c]+dfs(x-day[mx],mx-1,c);		
		return ans;
	}
}
void pre(){
	ll j,l;
	for (l= len,mx= 1;mx<=n&&l<=oo;mx++,l<<= 1){
		day[mx]%= len<<(mx-1);
		for (j= 0;j<26;j++)
			d[mx][j]= (sum[len][j]<<(mx-1))-dfs((len<<(mx-1))-day[mx],mx-1,j);
	}
}
int main()
{
	scanf("%s",s+1);
	len= strlen(s+1);
	for (i= 1;i<=len;i++)
		for (j= 0;j<26;j++)
			sum[i][j]= sum[i-1][j]+(s[i]-'a'==j);
	scanf("%lld%lld",&n, &m);
	for (i=1;i<=n;i++)
		scanf("%lld",&day[i]);
	pre();
	for (i= 1;i<=m;i++){
		ll l,r;
		scanf("%lld%lld%s",&l, &r, S+1);
		ans= dfs(r,mx,S[1]-'a')-dfs(l-1,mx,S[1]-'a');
		printf("%lld\n",ans);
	}return 0;
}
