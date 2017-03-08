#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int N, M;
int C[100100];
vector<int> G[100100];
bool visited[100100];
vector< pair<int, int> > Q[100100];
int ans[100100];

struct tally
{
	map<int, int> table;
	vector<int> num;
	tally(int c)
	{
		table[c] = 1;
		num.push_back(0);
		num.push_back(1);
	}
};
tally* T[100100];

void merge(tally* a, tally* b) // size of a >= size of b
{
	for(map<int, int>::iterator it = b->table.begin(); it != b->table.end(); it++)
	{
		int c = it->first, n = it->second;
		for(int i = a->table[c]+1; i <= a->table[c]+n; i++)
		{
			while(i >= a->num.size()) a->num.push_back(0);
			a->num[i]++;
		}
		a->table[c] += n;
	}
}

void dfs(int v, int p)
{
	T[v] = new tally(C[v]);
	for(int i = 0; i < G[v].size(); i++)
	{
		int w = G[v][i];
		if(w == p) continue;
		dfs(w, v);
		if(T[v]->table.size() >= T[w]->table.size())
			merge(T[v], T[w]);
		else
		{
			merge(T[w], T[v]);
			T[v] = T[w];
		}
	}
	for(int i = 0; i < Q[v].size(); i++)
	{
		int k = Q[v][i].first, q = Q[v][i].second;
		ans[q] = (k >= T[v]->num.size() ? 0 : T[v]->num[k]);
	}
}

int main()
{
	cin >> N >> M;
	for(int i = 1; i <= N; i++) cin >> C[i];
	for(int e = 1; e <= N-1; e++)
	{
		int a, b;
		cin >> a >> b;
		G[a].push_back(b);
		G[b].push_back(a);
	}
	for(int i = 1; i <= M; i++)
	{
		int v, k;
		cin >> v >> k;
		Q[v].push_back(make_pair(k, i));
	}
	dfs(1, -1);
	for(int i = 1; i <= M; i++) cout << ans[i] << '\n';
	return 0;
}
