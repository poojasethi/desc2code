#include <bits/stdc++.h>


using namespace std;
#define mp make_pair
#define pb push_back

map<int, set<pair<int, int> > > m;
vector<pair<int, int> > p;
vector<int> linha, coluna;

int main()
{
	int x, y;
	int n;
	int w;
	
	
	cin >> n;
	
	for (int i = 0; i < n ; ++i)
	{
		cin >> x >> y;
		
		m[y - x].insert(mp(x, y));
	}
	p.assign(n, pair<int, int>());
	for (int i = 0 ; i < n ; ++i)
	{
		cin >> w;
		
		if (!m.count(w))
		{
			cout << ("NO\n");
			return 0;
		}
		set<pair<int, int> > :: iterator it = m[w].begin();
		p[i] = (*it);
		m[w].erase(it);
	}
	linha.assign(n, -1);
	coluna.assign(n, -1);
	
	for (int i = 0; i < n ; ++i)
	{
		x = p[i].first;
		y = p[i].second;
		if (linha[x] != y - 1 || coluna[y] != x - 1)
		{
			cout << ("NO\n");
			return 0;
		}
		++linha[x];
		++coluna[y];
	}
	
	cout << ("YES\n");
	
	for (int i = 0 ; i < n ; ++i)
		cout << p[i].first << ' ' << p[i].second << '\n';
	return 0;
}
