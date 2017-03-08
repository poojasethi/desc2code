#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#define INF 1000000000
#define N 200100
using namespace std;
int p[N], C[N], V[N], nxt[N], S[N], Sn[N], q[N], vis[N], f[N], g[N], Id1[N], Id2[N];
int n, L, U, i, ed, G, Mx, Md, mc, now, l, r, mid, ans, AL, AR;
inline int gi()
{
    int ret = 0; char ch = getchar();
    while ((ch > '9' || ch < '0') && ch != '-') ch = getchar();
    while (ch <= '9' && ch >= '0') ret = ret * 10 + ch - '0', ch = getchar();
    return ret;
}
void Add(int u, int v, int c)
{
	C[++ed] = c, V[ed] = v, nxt[ed] = p[u], p[u] = ed;
}
void Dfs_G(int x, int fa)
{
	S[x] = 1, Sn[x] = 0;
	for (int i = p[x]; i != -1; i = nxt[i])
		if (V[i] != fa && !vis[V[i]])
		{
			Dfs_G(V[i], x);
			S[x] += S[V[i]];
			Sn[x] = max(Sn[x], S[V[i]]);
		}
	Sn[x] = max(Sn[x], now - S[x]);
	if (Sn[x] < Sn[G]) G = x;
}
void Dfs_d(int x, int fa, int dep, int d)
{
	if (dep > U) return;
	if (dep > Mx) Mx = dep;
	if (d > g[dep]) g[dep] = d, Id1[dep] = x;
	for (int i = p[x]; i != -1; i = nxt[i])
    {
		if (V[i] == fa || vis[V[i]]) continue;
		int z = ((C[i] - mid) >= 0 ? 1 : -1);
		Dfs_d(V[i], x, dep + 1, d + z);
	}
}
void Dfs(int x, int fa)
{
	S[x] = 1;
	for (int i = p[x]; i != -1; i = nxt[i])
		if (!vis[V[i]] && V[i] != fa)
			Dfs(V[i], x), S[x] += S[V[i]];
}
bool Calc(int x)
{
	Id2[0] = x;
	for (i = 1; i <= Md; i++) f[i] = -INF;
	vis[G] = 1, Md = 0;
	int mxx = -INF, mp = -1, i;
	for (i = p[x]; i != -1; i = nxt[i])
	{
		if (vis[V[i]]) continue;
		for (int j = 1; j <= Mx; j++) g[j] = -INF;
		Mx = 0;
		int z = ((C[i] - mid) >= 0 ? 1 : -1);
		Dfs_d(V[i], x, 1, z);
		int l = 1, r = 0, j, mn = min(Mx, U);
		if (mp != -1) q[++r] = mp;
		for (j = 1; j <= mn; j++)
		{
			while (l <= r && q[l] + j > U) l++;
			if (j <= L && Md + j >= L)
			{	
				while (l <= r && f[q[r]] < f[L - j]) r--;
				q[++r] = L - j;
				if (f[q[l]] + g[j] >= 0)
				{
					AL = Id2[q[l]], AR = Id1[j];
					return true;
				}
			}
			else if (j > L && f[q[l]] + g[j] >= 0)
			{
				AL = Id2[q[l]], AR = Id1[j];
				return true;
			}
		}
		Md = max(Md, Mx);
		for (int j = 1; j <= Mx; j++)
		{
			if (g[j] > f[j]) f[j] = g[j], Id2[j] = Id1[j];
			g[j] = -INF;
			if (j >= L && j <= U)
				if (f[j] > mxx) mxx = f[j], mp = j;
		}
	}
	return false;
}
void Divide(int x)
{
	Sn[G = 0] = INF;
	Dfs_G(x, 0);
	if (S[x] <= L) return;
	Dfs(G, 0);
	int l = ans, r = mc, can = 0.0;
	while (l <= r)
    {
		mid = (l + r) / 2;
		if (Calc(G)) l = mid + 1, can = mid;
		else r = mid - 1;
	}
	ans = max(can, ans);
	for (int i = p[G]; i != -1; i = nxt[i])
	{
		if (vis[V[i]]) continue;
		now = S[V[i]];
		Divide(V[i]);
	}
}
int main()
{
	memset(p, -1, sizeof(p));
	scanf("%d%d%d", &n, &L, &U);
	for (i = 1; i < n; i++)
	{
		int u = gi(), v = gi(), c = gi();
		mc = max(mc, c);
		Add(u, v, c), Add(v, u, c);
	}
	for (i = 1; i <= n; i++) f[i] = g[i] = -INF;
	now = n;
	Divide(1);
	printf("%d %d", AL, AR);
	return 0;
}