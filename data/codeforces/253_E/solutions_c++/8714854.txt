#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <string>
#include <queue>
using namespace std;
typedef long long LL;
const int Maxn=50005;
int n,w,need[Maxn],used[Maxn];
LL cur,T,last[Maxn];

template <class T>
inline void get(T &v) {
	bool f=false; char ch;
	while (!isdigit(ch=getchar())) f|=ch=='-';
	v=ch-48;
	while (isdigit(ch=getchar())) v=v*10+ch-48;
	if (f) v=-v;
}

struct Task{
	int t,s,p;
}t[Maxn];

struct info{
	int x,y;
	info(){}
	info(int x,int y):x(x),y(y){}
	bool operator <(const info &rhs)const{
		return x<rhs.x;
	}
}q[Maxn],g[Maxn];
priority_queue <info> h;

inline int calc(LL s1,LL t1,LL s2,LL t2) {
	return max(0LL,min(t1,t2)-max(s1,s2)+1);
}

void solve() {
	cur=0;	
	for (int i=1;i<=n;i++) {
		h.push(info(t[q[i].y].p,q[i].y));
		need[q[i].y]=t[q[i].y].s;
		cur=max(cur,LL(q[i].x));
		while ((i==n||cur<q[i+1].x)&&!h.empty()) {
			int x=h.top().y,d=i==n?need[x]:min(need[x],int(q[i+1].x-cur));
			used[x]+=calc(t[w].t,T-1,cur,cur+d-1); cur+=d;
			if ((need[x]-=d)==0) last[x]=cur,h.pop();
		}
	}
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	get(n);
	for (int i=1;i<=n;i++) {
		get(t[i].t); get(t[i].s); get(t[i].p);
		if (t[i].p==-1) w=i;
		q[i]=info(t[i].t,i);
	}
	get(T);
	sort(q+1,q+n+1);
	solve();
	for (int i=1;i<=n;i++) g[i]=info(t[i].p,i);
	sort(g+1,g+n+1);
	int j=1,sum=0;
	while (sum<t[w].s) sum+=used[g[j++].y];
	--j; sum=max(1,g[j].x+1);
	while (j<n&&g[j+1].x==sum) ++sum,j++;
	t[w].p=sum;
	printf("%d\n",t[w].p);
	solve();
	for (int i=1;i<=n;i++) printf("%I64d ",last[i]);
	return 0;
}