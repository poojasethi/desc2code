#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<queue>
#include<vector>
using namespace std;

const int mo=1000000007,N=300010;
int p[N],pn,f[N],inv[N],fac[N],sum[N];
int n,ans,a[N];
vector<int>v[N];

int ksm(int x,int y){
	int tmp=1;
	for(;y;y>>=1,x=1ll*x*x%mo)
	if(y&1) tmp=1ll*tmp*x%mo;
	return tmp;
}
void init(){
	for(int i=2;i<=300000;i++){
		if(!f[i]) p[++pn]=i;
		for(int j=1;j<=pn&&p[j]*i<=300000;j++){
			f[p[j]*i]=1;
			if(i%p[j]==0) break;
		}
	}
	fac[0]=1;
	for(int i=1;i<=n;i++) fac[i]=1ll*i*fac[i-1]%mo;
	inv[n]=ksm(fac[n],mo-2);
	for(int i=n-1;~i;i--) inv[i]=1ll*inv[i+1]*(i+1)%mo;
	sum[0]=1;
	for(int i=1;i<n;i++) 
	sum[i]=(sum[i-1]+1ll*fac[n-1]*inv[i]%mo*inv[n-1-i])%mo;
}
int solve(int x){
	int ans=0,s=v[x].size(),k;
	for(int i=0;i<s;i++){
		k=n-s+i;
		ans=(ans-1ll*v[x][i]*(sum[n-1]-sum[k]-sum[k-1])%mo)%mo;
	}
	return ans;
}
int main(){
	scanf("%d",&n);
	init();
	for(int i=1;i<=n;i++) scanf("%d",a+i);
	for(int i=1;i<=n;i++){
		for(int j=1;p[j]*p[j]<=a[i];j++)
		if(a[i]%p[j]==0){
			int s=0;
			while(a[i]%p[j]==0) s++,a[i]/=p[j];
			v[p[j]].push_back(s);
		}
		if(a[i]!=1) v[a[i]].push_back(1);
	}
	for(int i=1;i<=300000;i++)
	if(v[i].size()) sort(v[i].begin(),v[i].end());
	for(int i=1;i<=300000;i++)
	if(v[i].size()) ans=(ans+solve(i))%mo;
	if(ans<0) ans+=mo;
	printf("%d\n",ans);
	return 0;
}