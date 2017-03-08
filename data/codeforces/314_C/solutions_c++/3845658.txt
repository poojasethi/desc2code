#include<iostream>
#include<cstring>
#include<cstdlib>
#include<cstdio>
using namespace std;
const int N=100010,M=1000000,mod=1000000007;
int n,f[M+10],a[M+10];
inline void add(int &x,int y) {
	x+=y;
	if(x>=mod) x-=mod;
}
inline void update(int x,int y) {
	for(;x<=M;x+=x&-x) add(f[x],y);
}
inline int query(int x) {
	int tot=0;
	for(;x;x-=x&-x) add(tot,f[x]);
	return tot;
}
int main() {
	scanf("%d",&n);
	for(int i=1,x,y;i<=n;i++) {
		scanf("%d",&x);
		y=(query(x)+1ll)*x%mod;
		update(x,((y-a[x])%mod+mod)%mod);
		a[x]=y;
	}
	printf("%d\n",query(1000000));
	return 0;
}