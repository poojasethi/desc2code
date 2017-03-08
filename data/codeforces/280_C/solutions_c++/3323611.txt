#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;
const int MAX_N = 1e5+7;
vector<int> G[MAX_N];
int n;
double dfs(int x, int p, int l)
{
	double ret = 1.0/l;
	for (int i = 0; i < G[x].size(); i++) if (G[x][i] != p)
		ret += dfs(G[x][i], x, l+1);
	return ret;
}
int main()
{
	cin>>n;
	for (int i = 0; i < n-1; i++) {
		int a, b;
		cin>>a>>b;
		G[a].push_back(b);
		G[b].push_back(a);
	}
	printf ("%.12lf\n", dfs(1, -1, 1));
	return 0;
}