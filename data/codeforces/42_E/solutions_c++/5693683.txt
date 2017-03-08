#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<cstdio>
#define N 220000
#define rep(i,x,y) for(i=x;i<=y;++i)
using namespace std;
struct ppp{
	int x,y,k;
}e[N];
int cnt,n,m,i,j,k,bo[N],bo2[N],x,y,size[N],fa[N],d[N],p,qn;
long long ans;
bool cmp(const ppp&a,const ppp&b){
	return a.k<b.k;
}
int get(int x){
	while(fa[x])x=fa[x];
	return x;
}
int main(){
	scanf("%d%d",&n,&m);
	rep(i,1,m)scanf("%d%d%d",&e[i].x,&e[i].y,&e[i].k);
	sort(e+1,e+m+1,cmp);
	rep(i,1,n)size[i]=1;
	p=n;
	rep(i,1,m)if(get(x=e[i].x)!=get(y=e[i].y)){
		x=get(x); y=get(y);
		if(size[x]>size[y])swap(x,y);
		fa[x]=y; size[y]+=size[x];
		d[x]=e[i].k;
		ans+=e[i].k; p--;
	}
	scanf("%d",&qn);
	rep(i,1,qn){
		scanf("%d%d",&x,&y);
		++cnt; k=-1;
		for(j=x;j;k=max(k,d[j]),j=fa[j])bo[j]=cnt,bo2[j]=k;
		k=-1;
		for(j=y;j;k=max(k,d[j]),j=fa[j])if(bo[j]==cnt)break;
		if(p>2 || p==2 && j)puts("-1");
		else if(p==2)printf("%I64d\n",ans);
		else printf("%I64d\n",ans-max(k,bo2[j]));
	}
}
