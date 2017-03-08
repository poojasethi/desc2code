#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
using namespace std;

#define fillchar(a,x) memset(a,x,sizeof(a))

const int MAXN=100010;
const int MAXE=100010;

int g[MAXN], g_lnk[MAXE], g_nxt[MAXE];
int ea[MAXE], eb[MAXE], ec[MAXE];
int n, e;

int belong[MAXN], num;
int stack[MAXN], top;
int low[MAXN], dfn[MAXN], ttt;
void dfs(int x) {
	low[x]=dfn[x]=++ttt;
	stack[++top]=x;
	belong[x]=-1;
	for(int i=g[x]; i>0; i=g_nxt[i]) {
		int y=g_lnk[i];
		if(belong[y]==-1)
			low[x]=min(low[x], dfn[y]);
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

int ng[MAXN], ng_lnk[MAXE], ng_cst[MAXE], ng_ind[MAXE], ng_nxt[MAXE];
int p[MAXN], p_lnk[MAXN], p_nxt[MAXN];

int pre[MAXN];
int q[MAXN];
void bfs(int start) {
	fillchar(pre, 0);
	int ss=0, tt=1;
	pre[q[tt]=start]=-1;
	while(ss<tt) {
		int x=q[++ss];
		for(int i=ng[x]; i>0; i=ng_nxt[i]) {
			int y=ng_lnk[i];
			if(pre[y]==0) {
				if(ng_cst[i]==1) pre[y]=ng_ind[i];
				else pre[y]=-1;
				q[++tt]=y;
			} else {
				if(ng_cst[i]==0) pre[y]=-1;
			}
		}
	}
}

int le[MAXE], lecnt;
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d%d", &n, &e);
	fillchar(g, 0);
	for(int i=1, k=0; i<=e; ++i) {
		scanf("%d%d%d", &ea[i], &eb[i], &ec[i]);
		if(ec[i]==0) {
			++k;
			g_lnk[k]=eb[i], g_nxt[k]=g[ea[i]], g[ea[i]]=k;
		}
	}

	num=0; top=0; ttt=0;
	fillchar(belong, 0);
	for(int i=1; i<=n; ++i)
		if(belong[i]==0)
			dfs(i);
	fillchar(ng, 0);
	for(int i=1, k=0; i<=e; ++i) {
		int a=belong[ea[i]];
		int b=belong[eb[i]];
		if(a!=b) {
			++k;
			ng_lnk[k]=b, ng_cst[k]=ec[i], ng_ind[k]=i, ng_nxt[k]=ng[a], ng[a]=k;
		}
	}
	bfs(belong[1]);
	bool flag=true;
	lecnt=0;
	for(int i=1; i<=num; ++i) {
		if(pre[i]==0) flag=false;
		if(pre[i]>0) le[++lecnt]=pre[i];
	}
	if(flag) {
		printf("%d\n", lecnt);
		for(int i=1; i<=lecnt; ++i) printf("%d%c", le[i],i<lecnt?' ':'\n');
	} else
		printf("-1\n");
	return 0;
}
