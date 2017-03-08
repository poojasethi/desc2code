#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>
#include<cmath>
using namespace std;
const int maxn= 3e5;
vector<vector<int> > ans;
vector<int> g[maxn];
vector<int> p;
int mark[maxn],vis[maxn],fa[maxn];
int n,m,x,y,i,j,k;
void go(int x,int o){
	if (x!=o) go(fa[x],o);
	p.push_back(x);
}
int dfs(int o){
	vis[o]= 1;
	vector<int> s;
	s.clear();
	int len= g[o].size(),i;
	for (i= 0;i<len;i++){
		int v= g[o][i],t;
		if (vis[v]) continue;
		fa[v]= o;
		t= dfs(v);
		if (t!=-1)
			s.push_back(t);
	}
	if (mark[o])
		s.push_back(o);
	for (i= 0;i+1<(int)s.size();i+= 2){
		p.clear();
		int x= s[i],y= s[i+1];
		while (x!=o) p.push_back(x),x= fa[x];
		go(y,o);
		ans.push_back(p);
	}
	if ((int)s.size()&1) return s[s.size()-1];
	return -1;
}
int main()
{
	scanf("%d%d%d",&n, &m, &k);
	for (i= 1;i<=m;i++){
		scanf("%d%d",&x, &y);
		g[x].push_back(y);
		g[y].push_back(x);
	}
	for (i= 1;i<=k;i++){
		scanf("%d",&x);
		mark[x]= 1;
	}
	for (i= 1;i<=n;i++){
		if (vis[i]) continue;
		dfs(i);
	}
	printf("%d\n",(int)ans.size());
	for (i= 0;i<(int)ans.size();i++){
		int len= ans[i].size();
		printf("%d ",len-1);
		for (j= 0;j<len;j++)
			printf("%d%c",ans[i][j],j<len-1?' ':'\n');
	}
	return 0;
}
