#include <bits/stdc++.h>

using namespace std;

string s, t;
int yay, whoop;
int has[300];

int main()
{
	cin >> s >> t;
	for (int i = 0; i < s.length(); ++i)
		++has[s[i]];

	for (int i = 0; i < t.length(); ++i)
	{
		if (has[t[i]])
			++yay, --has[t[i]], t[i] = '-';
	}

	for (int i = 0; i < t.length(); ++i)
	if (t[i] != '-')
	{
		if (t[i] <= 'Z' && has[t[i] + 32])
			++whoop, has[t[i] + 32]--;
		else if (t[i] >= 'a' && has[t[i] - 32])
			++whoop, has[t[i] - 32]--;
	}

	cout << yay << ' ' << whoop;
	return 0;
}