#include<bits/stdc++.h>
using namespace std;

#define MAX 1005
#define INF 0x3f3f3f3f

map<char, int> dic;
const int neigh[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
int dp[MAX][MAX], mark[MAX][MAX], n, m;
char g[MAX][MAX];

inline bool can(int i, int j) { return (i>=0 && i<n && j>=0 && j<m); }

int opt(int i, int j)
{
	if(mark[i][j] == 1) return INF;
	int &state = dp[i][j];
	if(state != -1) return state;
	mark[i][j] = 1;

	int aux = (g[i][j] == 'A' ? 1 : 0);
	state = aux;
	for(int k=0; k<4; ++k)
	{
		int ni = i + neigh[k][0], nj = j + neigh[k][1]; 
		if(can(ni, nj) && dic[g[ni][nj]] == (dic[g[i][j]] + 1)%4) state = max(state, aux + opt(ni, nj));
	}
	
	mark[i][j] = 0;
	return state;
}

int main()
{
	dic['D'] = 0;
	dic['I'] = 1;
	dic['M'] = 2;
	dic['A'] = 3;

	scanf("%d %d", &n, &m);
	for(int i=0; i<n; ++i) scanf(" %s ", g[i]);

	memset(mark, 0, sizeof(mark));
	memset(dp, -1, sizeof(dp));
	int sol = 0;
	for(int i=0; i<n; ++i)
		for(int j=0; j<m; ++j)
			if(g[i][j] == 'D')
				sol = max(sol, opt(i, j));
	
	if(sol >= INF) puts("Poor Inna!");
	else if(sol == 0) puts("Poor Dima!");
	else printf("%d\n", sol);

	return 0;
}
