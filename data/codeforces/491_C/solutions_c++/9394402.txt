/***** MIN-COST FLOW *****/

#include <iostream>
#include <cstdio>
#include <queue>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;
const int MAX = 110;
const int INF = 1231231231;

vector<int> G[MAX];
int cap[MAX][MAX];
int cost[MAX][MAX];
int pi[MAX];
int dist[MAX];
int from[MAX];

int mcf(int src, int snk, int flow)
{
	for(int i = 0; i < MAX; i++)
		for(int j = 0; j < MAX; j++)
			if(cap[i][j])
				cost[j][i] = -cost[i][j];

	memset(pi, 0, sizeof(pi));

	int cst = 0;
	for(int f = 0; f < flow; )
	{
		for(int i = 0; i < MAX; i++) dist[i] = INF;
		memset(from, -1, sizeof(from));
		dist[src] = 0, from[src] = -2;
		priority_queue<pair<int, int> > q;
		q.push(make_pair(0, src));
		while(!q.empty())
		{
			pair<int, int> pr = q.top(); q.pop();
			int best = pr.second;
			if(abs(pr.first + dist[best]) > 0) continue;
			for(int vi = 0; vi < G[best].size(); vi++)
			{
				int i = G[best][vi];
				if(cap[best][i] && dist[best] + cost[best][i] + pi[best] - pi[i] < dist[i])
				{
					dist[i] = dist[best] + cost[best][i] + pi[best] - pi[i];
					from[i] = best;
					q.push(make_pair(-dist[i], i));
				}
			}
		}
		if(from[snk] == -1) return -1;
		for(int i = 0; i < MAX; i++) if(from[i] == -1) pi[i] += dist[i];

		int aug_f = flow - f;
		for(int v = snk; v != src; v = from[v])
			aug_f = min(aug_f, cap[from[v]][v]);

		for(int v = snk; v != src; v = from[v])
		{
			int u = from[v];
			cap[u][v] -= aug_f;
			cap[v][u] += aug_f;
			cst += aug_f * cost[u][v];
		}
		f += aug_f;
	}
	return cst;
}

void add_edge(int u, int v, int cp, int cst)
{
	G[u].push_back(v);
	G[v].push_back(u);
    cap[u][v] = cp;
    cap[v][u] = 0;
    cost[u][v] = cst;
}

#define SOURCE 107
#define SINK 108
#define IN(v) ((v) + 1)
#define OUT(v) ((v) + 53)

int N, K;
string A, B;
string table;

int main()
{
	for(char c = 'a'; c <= 'z'; c++) table += c;
	for(char c = 'A'; c <= 'Z'; c++) table += c;

	ios::sync_with_stdio(false);
	cin >> N >> K;
	cin >> A >> B;
	for(int i = 0; i < K; i++)
	{
		add_edge(SOURCE, IN(i), 1, 0);
		add_edge(OUT(i), SINK, 1, 0);
	}
	for(int ti = 0; ti < K; ti++)
	{
		char c = table[ti];
		int cnt[256];
		memset(cnt, 0, sizeof(cnt));
		for(int i = 0; i < N; i++)
			if(A[i] == c)
				cnt[B[i]]++;
		for(int i = 0; i < K; i++)
		{
			c = table[i];
			add_edge(IN(ti), OUT(i), 1, -cnt[table[i]]);
		}
	}
	int res = -mcf(SOURCE, SINK, K);
	cout << res << endl;
	for(int i = 0; i < K; i++)
		for(int j = 0; j < K; j++)
			if(cap[IN(i)][OUT(j)] == 0)
				cout << table[j];
}
