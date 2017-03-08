#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
int sg[44][44][44][44];
char mp[22][22];
int r;
int n, m;
int work(int a, int b, int c, int d)
{
	bool has[444] = {0};
	if (sg[a][b][c][d] != -1)
		return sg[a][b][c][d];
	int flg = 0;
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= m; j++)
			if (((i + j) & 1) == r && a < n - i + j + 1 && n - i + j + 1 < b && c < i + j  && i + j < d)
			{
				if (mp[i][j] == 'L')
					has[work(a, n - i + j + 1, c, d) ^ work(n - i + j + 1, b, c, d)] = 1;
				if (mp[i][j] == 'R')
					has[work(a, b, i + j, d) ^ work(a, b, c, i + j)] = 1;
				if (mp[i][j] == 'X')
					has[work(a, n - i + j + 1, i + j, d) ^ work(a, n - i + j + 1, c, i + j) ^ work(n - i + j + 1, b, i + j, d) ^ work(n - i + j + 1, b, c, i + j)] = 1;
			}
	for (int i = 0; i < 404; i++)
		if (!has[i])
		{
			sg[a][b][c][d] = i;
			break;
		}
	return sg[a][b][c][d];
}
int main()
{
	scanf("%d%d", &n, &m);
	for (int i = n; i >= 1; i--)
		scanf("%s", mp[i] + 1);
	memset(sg, -1, sizeof(sg));
	r = 0;
	int t = work(0, n + m + 2, 0, n + m + 2);
	r = 1;
	t ^= work(1, n + m + 1, 1, n + m + 1);
	if (t)
		printf("WIN");
	else
		printf("LOSE");
}
