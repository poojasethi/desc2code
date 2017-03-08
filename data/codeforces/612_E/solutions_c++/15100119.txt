#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>
#include<cmath>
#define rep(i,a,n) for (int i= a;i<=n;i++)
#define ll long long
using namespace std;
const int maxn= 2e6;
vector<int> a[maxn];
int P[maxn],Q[maxn],vis[maxn],b[maxn];
int i,j,n,lb,bl,x;
void go(int o){
	while (!vis[o]){
		vis[o]= 1;
		b[++lb]= o;
		o= P[o];
	}
}
int main()
{
	//freopen("1.in","r",stdin);
	//freopen("1.out","w",stdout);
	scanf("%d",&n);
	for (i= 1;i<=n;i++)
		scanf("%d",&P[i]);	
	for (i= 1;i<=n;i++){
		if (vis[i]) continue;
		lb= 0;
		go(i);
		if (lb&1){
			int m= lb/2+1;
			for (j= 1;j<m;j++){
				Q[b[j]]= b[m+j];
				Q[b[m+j]]= b[j+1];
			}
			Q[b[m]]= b[1];
		}else if (a[lb].size()){
			Q[b[1]]= a[lb][0];
			for (j= 1;j<=lb;j++){
				Q[a[lb][j-1]]= P[b[j]];
				Q[P[b[j]]]= P[a[lb][j-1]];
			}
			a[lb].clear();
		}else {
			for (j= 1;j<=lb;j++)
				a[lb].push_back(b[j]);
		}
	}
	bl= 1;
	for (i= 2;i<=n;i+= 2)
		if (a[i].size()){
			bl= 0;
			break;
		}
	if (bl)
		for (i= 1;i<=n;i++)
			printf("%d%c",Q[i],i<n?' ':'\n');
	else printf("-1");
	return 0;
}
