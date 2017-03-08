#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll n, q, x, le, chan;
int res[1000010], type;

int main()
{
	scanf("%lld %lld", &n, &q);

	while (q--)
	{
		scanf("%d", &type);
		if (type == 2)
		{
			if (le&1)
				--le, ++chan;
			else
				--chan, ++le;
		}
		else
		{
			scanf("%lld", &x);
			le += x, chan += x;
		}
	}
	le %= n, chan %= n;

	for (int i = 1; i <= n; ++i)
	if (i&1)
		res[(i + le - 1 + n*n) % n + 1] = i;
	else
		res[(i + chan - 1 + n*n) % n + 1] = i;

	for (int i = 1; i <= n; ++i)
		printf("%d ", res[i]);
	return 0;
}