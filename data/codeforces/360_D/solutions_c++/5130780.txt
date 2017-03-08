#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#define int64 long long
#define N 120000
using namespace std;
int n,m,p,b,x,i,a[N],d[N],q[N],qn,tot,ans,j,f[N];
int64 pow(int64 x,int64 y,int64 mo){
	int64 res=1;
	while(y){
		if(y&1)res=res*x%mo;
		x=x*x%mo;
		y/=2;
	}
	return res;
}
int main(){
	scanf("%d%d%d",&n,&m,&p);
	for(i=1;i<=n;++i)scanf("%d",&a[i]);
	b=0;
	for(i=1;i<=m;++i)scanf("%d",&x),b=__gcd(b,x);
	tot=0;
	for(i=1;i*i<=p-1;++i)if((p-1)%i==0){
		d[++tot]=i;
		if(i*i!=p-1)d[++tot]=(p-1)/i;
	}
	sort(d+1,d+tot+1);
	for(i=1;i<=n;++i){
		a[i]=pow(a[i],b,p);
		for(j=1;j<=tot;++j)if(pow(a[i],d[j],p)==1)break;
		q[i]=(p-1)/d[j];
	}
	sort(q+1,q+n+1);
	qn=unique(q+1,q+n+1)-q-1;
	for(i=qn;i>=1;--i){
		f[i]=(p-1)/q[i];
		for(j=i+1;j<=qn;++j)if(q[j]%q[i]==0)f[i]-=f[j];
		ans+=f[i];
	}
	printf("%d\n",ans);
}
