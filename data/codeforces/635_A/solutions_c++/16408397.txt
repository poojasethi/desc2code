#include <bits/stdc++.h>

using namespace std;

int r, c, n, k, x[100], y[100];

int main()
{
	cin >> r >> c >> n >> k;
	for (int i = 0; i < n; ++i)
	{
		cin >> x[i] >> y[i];
	}

	int res = 0;
	for (int sx = 1; sx <= r; ++sx)
	for (int sy = 1; sy <= c; ++sy)
	for (int ex = 1; ex <= r; ++ex)
	for (int ey = 1; ey <= c; ++ey)
	{
		int cnt = 0;
		for (int i = 0; i < n; ++i)
		if (x[i] >= sx && x[i] <= ex && y[i] >= sy && y[i] <= ey)
			++cnt;
		res += (cnt >= k);
	}

	cout << res;
	return 0;
}