#include <bits/stdc++.h>

using namespace std;

int n, a[1010];
vector<int> res;

int main()
{
	scanf("%d %d", &n, a);
	res.push_back(a[0]);

	for (int i = 1; i < n; ++i)
	{
		scanf("%d", a+i);
		if (__gcd(a[i], a[i-1]) != 1)
			res.push_back(1);
		res.push_back(a[i]);
	}

	printf("%d\n", res.size() - n);
	for (int i = 0; i < res.size(); ++i)
		printf("%d ", res[i]);
	return 0;
}