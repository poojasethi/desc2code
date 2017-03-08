#include <bits/stdc++.h>

using namespace std;

int n, t[51];
bool ck[1010];

int main()
{
	scanf("%d", &n);

	for (int i = 0; i < n; ++i)
		scanf("%d", t+i), ck[t[i]] = true;

	for (int i = 0; i < n; ++i)
	if (ck[t[i] - 1] && ck[t[i] + 1])
	{
		printf("YES");
		return 0;
	}

	printf("NO");
	return 0;
}