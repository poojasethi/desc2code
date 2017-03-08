#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#define int64 long long

using namespace std;

const int Maxn = 510000;

int fa[Maxn * 2], recentRaid[Maxn * 2];
int faU[Maxn * 2];
int64 sum[Maxn * 2];
int opt[Maxn][3];
int posU[Maxn], posM[Maxn];
int num[Maxn * 2];
pair<int, int> query[Maxn];
vector<pair<int, int> > calc[Maxn];
int64 ans[Maxn];
int totU, totM, tot;
int N, M;

int getFather1(int x)
{
	if (fa[x] == x)
		return x;
	getFather1(fa[x]);
	recentRaid[x] = max(recentRaid[x], recentRaid[fa[x]]);
	fa[x] = fa[fa[x]];
	return fa[x];
}

int getFather2(int x)
{
	if (faU[x] == x)
		return x;
	getFather2(faU[x]);
	if (faU[x] != faU[faU[x]]) sum[x] += sum[faU[x]];
	faU[x] = faU[faU[x]];
	return faU[x];
}

int main()
{
	//freopen("input", "r", stdin);

	scanf("%d%d", &N, &M);
	for (int i=1;i<=N;++i)
	{
		posU[i] = posM[i] = i;
		num[i] = 1;
	}
	for (int i=1;i<=N+M;++i)
	{
		fa[i] = i;faU[i] = i;
		recentRaid[i] = -1;
		sum[i] = 0;
	}
	totU = N;
	totM = N;
	tot = 0;
	for (int i=0;i<M;++i)
	{
		calc[i].clear();
		char st[10];
		scanf("%s", st);
		opt[i][0] = -1;
		int x, y;
		if (st[0] == 'U')
		{
			scanf("%d%d", &x, &y);
			opt[i][0] = 1;opt[i][1] = x;opt[i][2] = y;
		}
		if (st[0] == 'M')
		{
			scanf("%d%d", &x, &y);
			++ totM;
			int fax = getFather1(x);
			int fay = getFather1(y);
			fa[fax] = totM;fa[fay] = totM;posM[x] = totM;
		}
		if (st[0] == 'A')
		{
			scanf("%d", &x);
			opt[i][0] = 2;opt[i][1] = x;
		}
		if (st[0] == 'Z')
		{
			scanf("%d", &x);
			recentRaid[posM[x]] = i;
		}
		if (st[0] == 'Q')
		{
			scanf("%d", &x);
			int fax = getFather1(x);
			int raid = max(recentRaid[x], recentRaid[fax]);
			query[tot ++] = make_pair(raid, i);
			if (raid > -1) calc[raid].push_back(make_pair(x, tot - 1));
			calc[i].push_back(make_pair(x, tot - 1));
		}
	}
	memset(ans, 0, sizeof(ans));
	for (int i=0;i<M;++i)
	{
		if (opt[i][0] == 1)
		{
			++ totU;
			int x = opt[i][1], y = opt[i][2];
			int fax = getFather2(x);
			int fay = getFather2(y);
			faU[fax] = totU; faU[fay] = totU;
			num[totU] = num[posU[x]] + num[posU[y]];
			posU[x] = totU;
		}
		if (opt[i][0] == 2)
		{
			sum[posU[opt[i][1]]] += num[posU[opt[i][1]]];
		}
		for (int j=0;j<calc[i].size();++j)
		{
			int x = calc[i][j].first;
			int q = calc[i][j].second;
			getFather2(x);
			int64 res = sum[x];
			if (faU[x] != x) res += sum[faU[x]];
			if (query[q].first == i) ans[q] -= res;
			else ans[q] += res;
		}
	}

	for (int i=0;i<tot;++i)
		printf("%I64d\n", ans[i]);

	return 0;
}