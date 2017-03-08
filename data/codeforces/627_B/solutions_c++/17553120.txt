#include <bits/stdc++.h>

using namespace std;

int n, k, a, b, q, type, dd, aa, pp;
int bita[200010], bitb[200010], cnta[200010], cntb[200010];

void updateA(int x, int val)
{
	while (x <= 200000)
	{
		bita[x] += val;
		x += x&(-x);
	}
}

void updateB(int x, int val)
{
	while (x <= 200000)
	{
		bitb[x] += val;
		x += x&(-x);
	}
}

int getA(int x)
{
	int res = 0;
	while (x > 0)
	{
		res += bita[x];
		x -= x&(-x);
	}
	return res;
}

int getB(int x)
{
	int res = 0;
	while (x > 0)
	{
		res += bitb[x];
		x -= x&(-x);
	}
	return res;
}

int main()
{
	scanf("%d %d %d %d %d", &n, &k, &a, &b, &q);

	while (q--)
	{
		scanf("%d", &type);

		if (type == 1)
		{
			scanf("%d %d", &dd, &aa);
			int tmp = min(cnta[dd] + aa, a) - cnta[dd];
			if (tmp) updateA(dd, tmp);
			cnta[dd] += tmp;
			tmp = min(cntb[dd] + aa, b) - cntb[dd];
			if (tmp) updateB(dd, tmp);
			cntb[dd] += tmp;
		}
		else
		{
			scanf("%d", &pp);
			int res = getB(pp-1) + getA(200000) - getA(pp + k - 1);
			printf("%d\n", res);
		}
	}
	return 0;
}