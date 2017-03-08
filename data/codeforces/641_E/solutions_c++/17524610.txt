#include <bits/stdc++.h>

using namespace std;

typedef pair<int,int> pii;

const int MAXX = 1e9;

int n, a, t, x;
map<pii, int> bit;

void update(int tt, int xx, int val)
{
	while (tt <= MAXX)
	{
		bit[pii(tt, xx)] += val;
		tt += tt&(-tt);
	}
}

int get(int tt, int xx)
{
	int res = 0;
	while (tt > 0)
	{
		res += bit[pii(tt, xx)];
		tt -= tt&(-tt);
	}
	return res;
}

int main()
{
	scanf("%d", &n);
	while (n--)
	{
		scanf("%d %d %d", &a, &t, &x);
		if (a == 3)
			printf("%d\n", get(t, x));
		else if (a == 1)
			update(t, x, 1);
		else
			update(t, x, -1);
	}
	return 0;
}