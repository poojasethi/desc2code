#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

map<ll, int> cnt;
int n, res;
ll a[100010];

int main()
{
	scanf("%d", &n);

	for (int i = 1; i <= n; ++i)
	{
		scanf("%lld", a+i);
		a[i] += a[i-1];
		res = max(res, ++cnt[a[i]]);
	}

	printf("%d", n - res);
	return 0;
}