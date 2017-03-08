#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void)
{
	int n;
	
	cin >> n;
	int A[2001] = {0};
	vector <pair<int, int> > v(n+1);
	v[0] = make_pair(0, 0);
	for (int i = 1; i <= n; ++i)
	{
		int x;
		
		cin >> x;
		v[i] = make_pair(x, i);
		A[x]++;
	}
	int cnt = 0;
	for (int i = 1; i < 2001; ++i)
	{
		if (A[i] > 1)
			cnt += A[i];
	}
	if (cnt < 3)
	{
		cout << "NO" << endl;
		return 0;
	}
	cout << "YES" << endl;
	sort(v.begin(), v.end());
	for (int x = 1; x <= 3; ++x)
	{
		int swp_cnt = x;
		for (int i = 1; i <= n; ++i)
		{
			cout << v[i].second << " ";
			if (swp_cnt > 0 && v[i].first == v[i-1].first)
			{
				swp_cnt--;
				swap(v[i], v[i-1]);	
			}
		}
		cout << endl;
	}
	return 0;
}

