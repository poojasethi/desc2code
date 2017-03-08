//In the name of Allah
//
//
#include <cstdio>
#include <vector>
using namespace std;
template<class T> inline void smn(T &a,const T &b){if(b<a) a=b;}
const int MN=1000*100+1000;
vector <int> list[MN];
int par[MN];
int h[MN];
int up[MN];
bool mark[MN];
int n,m;
void dfs(int a)
{
	mark[a]=1;
	up[a]=h[a];
	for (int i=0;i<list[a].size();i++) if (!mark[list[a][i]])
	{
		int u=list[a][i];
		par[u]=a;
		h[u]=h[a]+1;
		dfs(u);
		smn(up[a],up[u]);
	}
	else if (list[a][i]!=par[a] && h[list[a][i]]<h[a])
		smn(up[a],h[list[a][i]]);
}
int main(int argc,char * argv[])
{
	scanf("%d %d",&n,&m);
	for (int i=0;i<m;i++)
	{
		int a,b;
		scanf("%d %d",&a,&b); a--; b--;
		list[a].push_back(b);
		list[b].push_back(a);
	}
	par[0]=-1;
	dfs(0);
	for (int i=1;i<n;i++) if (up[i]==h[i])
	{
		printf("0\n");
		return 0;
	}
	for (int i=0;i<n;i++) for (int j=0;j<list[i].size();j++)
	{
		int u=list[i][j];
		if (par[u]==i)
			printf("%d %d\n",i+1,u+1);
		else if (h[i]>h[u] && par[i]!=u)
			printf("%d %d\n",i+1,u+1);
	}
	return 0;
}
