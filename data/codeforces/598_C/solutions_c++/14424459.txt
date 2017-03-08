#include <bits/stdc++.h>

using namespace std;
typedef long double ld;
typedef pair<ld, int> pdi;
typedef long long ll;



int n;
vector< pdi > v;


bool comp(pdi a, pdi b)
{
	return a.first < b.first;
}
int main()
{
	ll x, y;
	ios_base :: sync_with_stdio(0);
	cin.tie(0);
	
	cin >> n;
	
	for(int i = 0; i < n; ++i)
	{
		cin >> x >> y;
		v.push_back(pdi(atan2((double)y, (double)x), i + 1));
	}
	sort(v.begin(), v.end(), comp);
	
	int idx1, idx2;
	ld mn = 1e10;
	
	for(int i = 0; i < n; ++i)
	{
		int j = (i + 1) % n;
		ld d = v[j].first - v[i].first;
		if (d < 0) d += 2 * acos(-1);
		if(mn > d)
		{
			mn = d;
			idx1 = v[i].second;
			idx2 = v[j].second;
		}
	}
	
	cout << idx1 << ' ' << idx2 << '\n';
	return 0;
}
