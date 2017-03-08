#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<vector>
#define N 2011
using namespace std;
int L[N],R[N],P[2*N],f[2*N],key[2*N],ans[N][N],n,i,j,id[N],maxx,k,x,p[N],y;
vector <int> E[2*N];
int Find(int x){
	return lower_bound(P+1,P+n+n+1,x)-P;
}
bool cmp(const int&a,const int&b){
	return R[a]<R[b] || R[a]==R[b] && L[a]>L[b];
}
int main(){
	scanf("%d",&n);
	for(i=1;i<=n;++i){
		scanf("%d%d",&x,&y);
		P[i]=L[i]=x-y; P[i+n]=R[i]=x+y;
		id[i]=i;
	}
	sort(P+1,P+n+n+1);
	for(i=1;i<=n;++i)L[i]=Find(L[i]),R[i]=Find(R[i]);
	L[n+1]=0; R[n+1]=n+n;  id[n+1]=n+1;
	++n;
	sort(id+1,id+n+1,cmp);
	for(int t=1;t<=n;++t){
		i=id[t];
		memset(f,255,sizeof(f));
		f[L[i]]=0; key[L[i]]=0;
		maxx=0;
		for(j=L[i]+1;j<=R[i];++j){
			f[j]=f[j-1];
			key[j]=key[j-1];
			for(k=0;k<E[j].size();++k){
				x=E[j][k];
				if(L[x]<L[i])continue;
				if(f[L[x]]+p[x]>f[j]){
					f[j]=f[L[x]]+p[x];
					key[j]=x;
				}
			}
		}
		k=R[i];
		p[i]=f[R[i]]+1;
		while(true){
			x=key[k];
			if(!x)break;
			for(j=1;j<=ans[x][0];++j)
				ans[i][++ans[i][0]]=ans[x][j];
			k=L[x];
		}
		ans[i][++ans[i][0]]=i;
		E[R[i]].push_back(i);
	}
	printf("%d\n",p[n]-1);
	for(i=1;i<ans[n][0];++i)printf("%d ",ans[n][i]);
	return 0;
}