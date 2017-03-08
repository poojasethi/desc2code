#include <bits/stdc++.h>

using namespace std;

int maxpre, maxsuf, n;
char s[1000010], t[1000010];

int main()
{
	scanf("%s %s", s+1, t+1);
	n = strlen(s+1);

	maxpre = 1;
	while (s[maxpre] == t[maxpre])
		++maxpre;
	--maxpre;
	maxsuf = n;
	while (s[maxsuf] == t[maxsuf - 1])
		--maxsuf;
	++maxsuf;

	vector<int> res;
	for (int i = maxsuf - 1; i <= maxpre + 1; ++i)
		res.push_back(i);

	printf("%d\n", (int)res.size());
	for (int i = 0; i < (int)res.size(); ++i)
		printf("%d ", res[i]);
	return 0;
}