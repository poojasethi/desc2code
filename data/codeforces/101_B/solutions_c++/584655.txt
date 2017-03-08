#include <stdio.h>
#include <string.h>
#include <algorithm>
#define maxn 100010
#define mod 1000000007
struct node{
	int st,en;
	friend bool operator < (const node &x,const node &y){
		return x.en<y.en;
	}
} a[maxn];
int t[maxn];
int n,m;
int ans;
void ins(int p,int v){
	for (;p<=m;p+=(p&(p^(p-1)))) t[p]=(t[p]+v)%mod;
}
int ask(int p){
	int ret=0;
	for (;p;p-=(p&(p^(p-1)))) ret=(ret+t[p])%mod;
	return ret;
}
int main(){
	scanf("%d%d",&n,&m);
	for (int i=1;i<=m;i++) scanf("%d%d",&a[i].st,&a[i].en);
	std::sort(a+1,a+m+1);
	int ans=0;
	for (int i=1,j=0;i<=m;i++){
		while (j<i-1 && a[j+1].en<a[i].en) j++;
		int v=0;
		if (a[i].st==0) v++;
		int L=1,R=j,mid;
		int k=j+1;
		while (L<=R){
			mid=(L+R)>>1;
			if (a[mid].en>=a[i].st){
				k=mid;
				R=mid-1;
			}else L=mid+1;
		}
		if (k<=j) v+=ask(j)-ask(k-1);
		v+=mod;
		v%=mod;
		if (a[i].en==n) ans=(ans+v)%mod;
		ins(i,v);
	}
	printf("%d\n",ans);
	return 0;
}