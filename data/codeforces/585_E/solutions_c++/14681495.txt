#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>
#include<cmath>
#define ll long long
using namespace std;
const int maxn= 1e7+2,mo= 1e9+7;
int miu[maxn],cnt[maxn],xp[maxn];
int i,j,ans,n,x;
int main()
{
	//freopen("1.in","r",stdin);
	//freopen("1.out","w",stdout);
	xp[0]= 1;
	for (i= 1;i<maxn;i++)
		xp[i]= xp[i-1]*2%mo;
	scanf("%d",&n);
	for (i= 1;i<=n;i++){
		scanf("%d",&x);
		cnt[x]++;
	}
	miu[1]= 1;
	for (i= 1;i<maxn;i++){
		for (j= 2*i;j<maxn;j+= i){
			miu[j]-= miu[i];
			cnt[i]+= cnt[j];
		}
		ans= (ans+(long long)miu[i]*(xp[cnt[i]]-1)*(cnt[i]-n)%mo)%mo;
	}
	ans= (ans+mo)%mo;
	printf("%d",ans);
	return 0;		
}
