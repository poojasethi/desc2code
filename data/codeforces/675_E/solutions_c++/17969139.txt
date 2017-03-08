#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int n, a[100010], mn[100010][20], myPow[20];
ll f[100010], sum;

void init()
{
	myPow[0] = 1;
	for (int i = 1; i < 20; ++i)
		myPow[i] = (myPow[i-1] << 1);

	for (int i = n+1; --i; )
	{
		mn[i][0] = i;
		for (int j = 1; i + myPow[j] - 1 <= n; ++j)
		{
			if (a[mn[i][j-1]] < a[mn[i + myPow[j-1]][j-1]])
				mn[i][j] = mn[i + myPow[j-1]][j-1];
			else
				mn[i][j] = mn[i][j-1];
		}
	}
}

int query(int lef, int rig)
{
	int len = rig - lef + 1;
	int k = 20, res = lef;

	while (len)
	{
		while (myPow[--k] > len);
		if (a[mn[lef][k]] > a[res])
			res = mn[lef][k];
		lef += myPow[k];
		len -= myPow[k];
	}
	return res;
}

int main()
{
	scanf("%d", &n);

	for (int i = 1; i < n; ++i)
		scanf("%d", a+i);
	a[n] = n;
	init();

	for (int i = n; --i; )
	{
		int m = query(i+1, a[i]);
		f[i] = f[m] - (a[i] - m) + n - i;
		// cout << i << ' ' << m << ' ' << f[i] << '\n';
		sum += f[i];
	}

	printf("%lld", sum);
	return 0;
}