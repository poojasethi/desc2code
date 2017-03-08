#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <queue>
#include <algorithm>

using namespace std;

#define clr(f,x) memset(f,x,sizeof f)
#define rep(it,a,b) for(int it=a;it<=b;++it)
#define For_edge(p,x) for(int p=H[x];p;p=X[p])
#define _rep(it,a,b) for(int it=a;it>=b;--it)
#define PII pair<int,int>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define lb lower_bound
#define LL long long
queue<PII> Q;
int n,ans;
PII t[3],ret[1000010];
inline void add(PII &a,PII &b){
	ret[++ans]=mp(a.se,b.se);
	b.fi-=a.fi,a.fi<<=1;
}
inline void work(PII *t){
	if(t[0].fi==0)return;
	int x=t[1].fi/t[0].fi;
	for(;x;x>>=1){
		if(x&1)add(t[0],t[1]);
		else add(t[0],t[2]);
	}
	sort(t,t+3);
	work(t);
}
int main(){
	scanf("%d",&n);
	int x;
	rep(i,1,n){
		scanf("%d",&x);
		if(x)Q.push(mp(x,i));
	}
	int num=Q.size();
	if(num<=1)return puts("-1"),0;
	if(num==2)return puts("0"),0;
	rep(i,1,num-2){
		t[0]=Q.front(),Q.pop();
		t[1]=Q.front(),Q.pop();
		t[2]=Q.front(),Q.pop();
		sort(t,t+3);
		work(t);
		Q.push(t[1]),Q.push(t[2]);
	}
	printf("%d\n",ans);
	rep(i,1,ans)printf("%d %d\n",ret[i].fi,ret[i].se);
	return 0;
}