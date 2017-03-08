#include <bits/stdc++.h>


using namespace std;

void print(vector<pair<int, int> > &v)
{
	for (int i = 0 ; i < v.size(); ++i)
		cout << v[i].second + 1 << ' ' ;
	cout << '\n';
}
int main()
{
	vector<pair<int, int> > v;
	vector<pair<int, int> > troca;
	
	int n;
	int x;
	cin >> n;
	
	for (int i = 0 ; i < n ; ++i)
	{
		cin >> x;
		v.push_back(make_pair(x, i));
	}
	
	sort(v.begin(), v.end());
	
	
	for (int i = 1; i < n  && troca.size() < 2; ++i)
	{
		if (v[i].first == v[i - 1].first)
			troca.push_back(make_pair(i - 1, i));
	}
	
	if (troca.size() < 2)
		cout << "NO\n";
	else
	{
		cout << "YES\n";
		print(v);
		swap(v[troca[0].first], v[troca[0].second]);
		print(v);
		swap(v[troca[1].first], v[troca[1].second]);
		print(v);	
	}
	
}
