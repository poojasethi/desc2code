#include <bits/stdc++.h>

using namespace std;

bool myCmp(string x, string y) { return (x + y < y + x); }

int n;
string s[50010];

int main()
{
	ios_base::sync_with_stdio(0);
	cin >> n;
	for (int i = 0; i < n; ++i)
		cin >> s[i];
	sort(s, s+n, myCmp);

	for (int i = 0; i < n; ++i)
		cout << s[i];
	return 0;
}