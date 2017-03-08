#include <bits/stdc++.h>

using namespace std;

int q;
map<string, string> mp;
string u, v;

int main()
{
	cin >> q;
	while (q--)
	{
		cin >> u >> v;
		if (mp.find(u) == mp.end())
			mp[v] = u;
		else
		{
			mp[v] = mp[u];
			mp.erase(u);
		}
	}

	cout << mp.size() << '\n';
	for (map<string,string>::iterator it = mp.begin(); it != mp.end(); ++it)
		cout << it->second << ' ' << it->first << '\n';
	return 0;
}