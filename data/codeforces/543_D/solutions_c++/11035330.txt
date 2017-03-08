#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
const ll mod = 1000000007;

int N, M;
vector<int> G[200005];
int P[200005];
int I[200005];
ll down[200005];
ll up[200005];

vector<ll> L[200005], R[200005];

int main()
{
	cin >> N;
	for(int i = 2; i <= N; i++)
	{
		int p;
		cin >> p;
		P[i] = p;
		G[p].push_back(i);
	}
	for(int u = N; u >= 1; u--)
	{
		down[u] = 1;
		for(int i = 0; i < G[u].size(); i++)
		{
			int v = G[u][i];
			I[v] = i;
			down[u] = (down[u] * (1 + down[v])) % mod;
		}
		if(G[u].empty()) continue;
		L[u] = vector<ll>(G[u].size());
		R[u] = L[u];
		L[u][0] = 1;
		for(int i = 0; i < G[u].size() - 1; i++)
		{
			int v = G[u][i];
			L[u][i + 1] = (L[u][i] * (1 + down[v])) % mod;
		}
		R[u][G[u].size() - 1] = 1;
		for(int i = G[u].size() - 1; i >= 1; i--)
		{
			int v = G[u][i];
			R[u][i - 1] = (R[u][i] * (1 + down[v])) % mod;
		}
	}
	for(int u = 1; u <= N; u++)
	{
		if(P[u])
		{
			int p = P[u], i = I[u];
			up[u] = (1 + (up[p] * ((L[p][i] * R[p][i]) % mod))) % mod;
		}
		else up[u] = 1;
	}
	for(int i = 1; i <= N; i++)
		cout << (up[i] * down[i]) % mod << ' ';
}
