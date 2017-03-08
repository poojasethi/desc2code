#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

const int MAXN=100010;
const int MAXE=100010;

int ea[MAXE], eb[MAXE], ec[MAXE], enxt[MAXE], e;
int g[MAXN];
int n;

int dfn[MAXN], low[MAXN], ttt;
int belong[MAXN], num;
int stack[MAXN], top;
void dfs(int x) {
	low[x]=dfn[x]=++ttt;
	stack[++top]=x;
	belong[x]=-1;
	for(int i=g[x]; i>0; i=enxt[i]) {
		int y=eb[i];
		if(belong[y]==-1) low[x]=min(low[x], dfn[y]);
		if(belong[y]==0) {
			dfs(y);
			low[x]=min(low[x], low[y]);
		}
	}
	if(low[x]==dfn[x]) {
		++num;
		do {
			belong[stack[top--]]=num;
		} while(stack[top+1]!=x);
	}
}

int q[MAXN], pre[MAXN];
int anse[MAXN];
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d%d", &n,&e);
	memset(g, 0, sizeof(g));
	for(int i=1; i<=e; ++i) {
		int a, b, c; scanf("%d%d%d", &a,&b,&c);
		ea[i]=a;
		eb[i]=b;
		ec[i]=c;
		if(c==0) enxt[i]=g[a], g[a]=i;
	}

	top=ttt=num=0;
	memset(belong, 0, sizeof(belong));
	for(int i=1; i<=n; ++i)
		if(belong[i]==0)
			dfs(i);
	memset(g, 0, sizeof(g));
	for(int i=1; i<=e; ++i) {
		int a=belong[ea[i]];
		int b=belong[eb[i]];
		if(a!=b) enxt[i]=g[a], g[a]=i;
	}

	//for(int i=1; i<=n; ++i)printf("%d\n", belong[i]);

	int ss=0, tt=1;
	memset(pre, 0, sizeof(pre));
	pre[q[tt]=belong[1]]=-1;
	while(ss<tt)
		for(int x=q[++ss], i=g[x]; i>0; i=enxt[i]) {
			int y=belong[eb[i]];
			if(pre[y]==0) {
				pre[y]=(ec[i]>0?i:-1);
				q[++tt]=y;
			} else if(ec[i]==0) pre[y]=-1;
		}
	int ans=0;
	for(int i=1; i<=num; ++i) if(pre[i]>0) anse[++ans]=pre[i];
	for(int i=1; i<=num; ++i) if(pre[i]==0) ans=-1;
	printf("%d\n", ans);
	for(int i=1; i<=ans; ++i) printf("%d%c", anse[i], i<ans?' ':'\n');
	return 0;

}
