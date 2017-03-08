#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>
#include<cmath>
#include<set>
#define ll long long
using namespace std;
const int maxn= 3e5;
struct node{
	int a,b,c,d,h;
	bool operator <(const node x)const{
		return b<x.b;
	};
};
struct que{
	int x,y,s,h;
};
queue<que> Q;
node P[maxn];
int d[maxn],b[maxn],p[maxn];
multiset<node> f[maxn];
node now;
int n,m,i,j,x1,x2,x3,x4,la,bl,h;
int lowbit(int o){
	return o&-o;
}
void add(int o,int n,node x){
	while (o<=n){
		f[o].insert(x);
		o+= lowbit(o);
	}
}
void print(int o){
	if (!o) return;
	print(p[o]);
	if (o!=n) printf("%d ",o);
	else printf("%d\n",o);
}
int main()
{
	//freopen("1.in","r",stdin);
	//freopen("1.out","w",stdout);
	scanf("%d",&n);
	d[la= 1]= 0;
	for (i= 1;i<=n;i++){
		scanf("%d%d%d%d",&x1, &x2, &x3, &x4);
		d[++la]= x1;
		d[++la]= x3;
		P[i]= (node){x1,x2,x3,x4,i};
	}
	sort(d+1,d+la+1);
	la= unique(d+1,d+la+1)-d-1;
	for (i= 1;i<=n;i++){
		P[i].a= lower_bound(d+1,d+la+1,P[i].a)-d;
		P[i].c= lower_bound(d+1,d+la+1,P[i].c)-d;
	}
	for (i= 1;i<=n;i++)
		add(P[i].a,la,P[i]);
	Q.push((que){1,0,0,0});
	while (!Q.empty()){
		que u= Q.front();
		Q.pop();
		int o= u.x;
		while (o){
			while (!f[o].empty()&&f[o].begin()->b<=u.y){
				now= *f[o].begin();
				f[o].erase(f[o].begin());
				if (b[now.h]) continue;
				b[now.h]= 1;
				p[now.h]= u.h;
				if (now.h==n){
					bl= u.s+1;
					goto pn;
				}
				Q.push((que){now.c,now.d,u.s+1,now.h});
			}
			o-= lowbit(o);
		}
	}
 pn:
	if (!bl){
		printf("-1");
		return 0;
	}else {
		printf("%d\n",bl);
		print(n);
	}
	return 0;
}
