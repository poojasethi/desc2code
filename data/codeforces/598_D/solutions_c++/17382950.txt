#include <bits/stdc++.h>

using namespace std;

int r, m, k, X, Y, res[1010][1010];
char grid[1010][1010];
bool v[1010][1010];
int dx [4] = {0, 0, 1, -1};
int dy [4] = {1, -1, 0, 0};

int dfs(int x, int y){
	v[x][y] = true;
	int ans = 0;
	for (int i = 0; i < 4; i++){
		if( grid[x + dx[i]][y + dy[i]] == '*')
			ans++;
		else if (!v[x + dx[i]][y + dy[i]])
			ans += dfs(x + dx[i], y + dy[i]);
	}
	return ans;
}

void dfs2(int x, int y, int ma){
	res[x][y] = ma;
	for (int i = 0; i < 4; i++)
		if (grid[x + dx[i]][y + dy[i]] == '.' && !res[x + dx[i]][y + dy[i]])
			dfs2(x + dx[i], y + dy[i], ma);
	
}

int main(){

	scanf("%d %d %d", &r, &m, &k);
	for (int i = 1; i <= r; i++)
		for(int j = 1; j <= m; j++)
			cin >> grid[i][j];
	
	while (k--){
		scanf("%d %d", &X, &Y);
		if (!res[X][Y])
			dfs2(X, Y, dfs(X, Y));
			
		printf("%d\n", res[X][Y]);
	}
}
