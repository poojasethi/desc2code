#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

int R[200005];
int num_comps = 0;

bool modify = false;
vector<pair<int, int> > history;
void restore()
{
	//printf("restoring %d\n", (int)(history.size()));
	for(int i = history.size() - 1; i >= 0; i--)
	{
		//printf("restoring %d %d\n", history[i].first, history[i].second);
		R[history[i].first] = history[i].second;
	}
	history.clear();
}

void init(int n)
{
	for(int i = 0; i <= n; i++) R[i] = -1;
	num_comps = n;
}
int find(int u)
{
	while(R[u] >= 0) u = R[u];
	return u;
}
void uni(int u, int v)
{
	u = find(u);
	v = find(v);
	if(u == v) return;
	if(modify)
	{
		history.push_back(make_pair(u, R[u]));
		history.push_back(make_pair(v, R[v]));
	}
	if(-R[u] < -R[v]) R[u] = v;
	else if(-R[u] > -R[v]) R[v] = u;
	else
	{
		R[u] = v;
		R[v]--;
	}
	num_comps--;
}

#define SEG 444

int N, M, Q;
//vector<int> G[200005];
pair<int, int> E[200005];
pair<int, int> query[200005];
int ans[200005];

vector<int> qid[200005];

int get(int l, int r)
{
	//printf("getting %d %d\n", l, r);
	modify = true;
	for(int i = l; i <= r; i++)
	{
		//printf("unioning %d %d\n", E[i].first, E[i].second);
		uni(E[i].first, E[i].second);
	}
	//printf("R is ");
	//for(int i = 1; i <= N; i++) printf("%d ", R[i]);
	//printf("\n");
	int res = num_comps;
	restore();
	//printf("resetted: R is ");
	//for(int i = 1; i <= N; i++) printf("%d ", R[i]);
	//printf("\n");
	modify = false;
	num_comps = N;
	return res;
}

int main2()
{
	cin >> N >> M >> Q;
	//for(int i = 0; i <= N; i++) G[i].clear();
	for(int i = 0; i < M / SEG + 10; i++) qid[i].clear();
	for(int i = 0; i <= M; i++) qid[i].clear();
	
	for(int i = 1; i <= M; i++) scanf("%d %d", &(E[i].first), &(E[i].second));
	
	init(N);
	for(int i = 1; i <= Q; i++)
	{
		scanf("%d %d", &(query[i].first), &(query[i].second));
		if(query[i].second - query[i].first <= SEG + 5)
		{
			ans[i] = get(query[i].first, query[i].second);
		}
		else qid[query[i].second].push_back(i);
	}
	
	for(int s = SEG; s <= M; s += SEG)
	{
		init(N);
		for(int v = s; v <= M; v++)
		{
			uni(E[v].first, E[v].second);
			for(int i = 0; i < qid[v].size(); i++)
			{
				int id = qid[v][i];
				int u = query[id].first;
				if(0 <= s - u && s - u < SEG)
				{
					int old = num_comps;
					modify = true;
					for(int j = s - 1; j >= u; j--) uni(E[j].first, E[j].second);
					ans[id] = num_comps;
					restore();
					num_comps = old;
					modify = false;
				}
			}
		}
	}
	
	for(int i = 1; i <= Q; i++) printf("%d\n", ans[i]);
}

int main()
{
	int T;
	cin >> T;
	while(T--) main2();
}