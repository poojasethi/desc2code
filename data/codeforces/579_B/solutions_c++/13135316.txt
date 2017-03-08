#include <cstdio>
#include <queue>
using std::priority_queue;
struct Node{
	int x, y, v;
	bool operator < (const Node &b) const
	{
		return v < b.v;
	}
};
int n;
int team[1010];
priority_queue<Node> Q;
int main()
{
	scanf("%d", &n);
	for(int i = 2; i <= n + n; i++)
		for(int j = 1; j < i; j++)
		{
			int x; scanf("%d", &x);
			Q.push((Node){i, j, x});
		}
	while(!Q.empty())
	{
		Node now = Q.top(); Q.pop();
		if(team[now.x] || team[now.y]) continue;
		team[now.x] = now.y;
		team[now.y] = now.x;
	}
	for(int i = 1; i <= n + n; i++) printf("%d ", team[i]);
	return 0;
}
