#include <bits/stdc++.h>

using namespace std;

int n, q, type, x;
int cnt[300010], cntsum, out, cntin[300010];
queue<int> qu;

int main()
{
	scanf("%d %d", &n, &q);

	while (q--)
	{
		scanf("%d %d", &type, &x);
		if (type == 1) {
			qu.push(x);
			++cntin[x];
		} else if (type == 2) {
			cntsum += (cntin[x] - cnt[x]);
			cnt[x] = cntin[x];
		} else if (x > out) {
			x -= out;
			out = x + out;
			for (int i = 0; i < x; ++i)
			{
				int xx = qu.front();
				if (cnt[xx]) {
					--cnt[xx];
					--cntsum;
				}
				--cntin[xx];
				qu.pop();
			}
		}

		printf("%d\n", (int)qu.size() - cntsum);
	}
	return 0;
}