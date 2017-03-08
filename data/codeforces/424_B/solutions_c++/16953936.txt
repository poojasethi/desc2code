#include <bits/stdc++.h>

using namespace std;

typedef pair<int,int> pii;

#define F first
#define S second

int n, s, x, y;
pii a[1010];

int main()
{
	scanf("%d %d", &n, &s);

	for (int i = 0; i < n; ++i)
	{
		scanf("%d %d %d", &x, &y, &a[i].S);
		a[i].F = x*x + y*y;
	}

	sort(a, a+n);

	for (int i = 0; i < n; ++i)
	{
		if (s + a[i].S >= 1000000)
		{
			printf("%.9lf", sqrt((double)a[i].F));
			return 0;
		}

		s += a[i].S;
	}

	printf("-1");
	return 0;
}