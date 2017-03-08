#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
using namespace std;
typedef long long ll;

const int INF=0x3f3f3f3f;
const int maxn=2e5+5;

int a[maxn],b[maxn],t[maxn],c[maxn];
ll mincost[maxn],mind[maxn],minp[maxn];
int mindd[maxn],minpp[maxn];
int k,m,s;

struct gad{
	ll cost;
	int num;
	bool operator < (const gad a)const{
		return cost<a.cost;
	}
}g[maxn];

bool cmp(gad a,gad b){
	return a.num<b.num;
}

bool check(int mid){
	ll sum=0;
	for(int i=1;i<=m;++i){
		if(t[i]==1){
			mincost[i]=mind[mid]*c[i];
		}
		else mincost[i]=minp[mid]*c[i];
	}
	sort(mincost+1,mincost+m+1);
	for(int i=1;i<=k;++i){
		sum+=mincost[i];
	}
	if(sum<=s)return 1;
	else return 0;
}

void print(int mid){
	printf("%d\n",mid);
	for(int i=1;i<=m;++i){
		g[i].num=i;
		if(t[g[i].num]==1){
			g[i].cost=mind[mid]*c[i];
		}
		else g[i].cost=minp[mid]*c[i];
	}
	sort(g+1,g+m+1);
	sort(g+1,g+k+1,cmp);
	for(int i=1;i<=k;++i){
		printf("%d %d\n",g[i].num,t[g[i].num]==1?mindd[mid]:minpp[mid]);
	}
}

int main(){
	int n;
	scanf("%d%d%d%d",&n,&m,&k,&s);
	mind[0]=minp[0]=INF;
	for(int i=1;i<=n;++i){
		scanf("%d",&a[i]);
		if(a[i]<mind[i-1]){
			mind[i]=a[i];
			mindd[i]=i;
		}
		else{
			mind[i]=mind[i-1];
			mindd[i]=mindd[i-1];
		}
	}
	for(int i=1;i<=n;++i){
		scanf("%d",&b[i]);
		if(b[i]<minp[i-1]){
			minp[i]=b[i];
			minpp[i]=i;
		}
		else{
			minp[i]=minp[i-1];
			minpp[i]=minpp[i-1];
		}
	}
	for(int i=1;i<=m;++i){
		scanf("%d%d",&t[i],&c[i]);
	}
	int l=1,r=n;
	int ans=n+1;
	while(l<=r){
		int mid=(l+r)>>1;
	//	printf("%d\n",mid);
		if(check(mid)){
			ans=min(ans,mid);
			r=mid-1;
		}
		else l=mid+1;
	}
	if(ans==n+1)printf("-1\n");
	else print(ans);
	return 0;
}
