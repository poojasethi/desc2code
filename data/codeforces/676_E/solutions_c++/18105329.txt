#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
const ll MOD1 = 1e9 + 7;
const ll MOD2 = 999999993;
const ll INF = 1e18;

int n, cnt;
ll k, a[100010], res1, res2;
char s[8];

int main()
{
	scanf("%d %lld", &n, &k);

	for (int i = 0; i <= n; ++i)
	{
		scanf("%s", s);
		if (s[0] == '?')
			a[i] = INF;
		else
			sscanf(s, "%lld", a+i), ++cnt;
	}

	if (!k)
	{
		if (a[0] == INF)
			return printf((cnt&1)?"Yes":"No"), 0;
		return printf(a[0]?"No":"Yes"), 0;
	}

	if (cnt <= n)
		return printf((n&1)?"Yes":"No"), 0;

	for (int i = n; i >= 0; --i)
	{
		res1 = ((res1*k + MOD1) % MOD1 + a[i] + MOD1) % MOD1;
		res2 = ((res2*k + MOD2) % MOD2 + a[i] + MOD2) % MOD2;
	}

	printf((res1||res2)?"No":"Yes");
	return 0;
}