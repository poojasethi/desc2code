/* bhupkas */

using namespace std;

#include "bits/stdc++.h"

int main()
{
	int t;
	vector < int > v,v1;
	cin >> t;
	int n;
	int num;
	int ans;
	for(int tc = 1 ; tc <= t ; tc++)
	{
		ans = 0;
		cin >> n;
		v.clear();
		v1.clear();
		for(int i = 0 ; i < n ; ++i)	cin >> num , v.push_back(num);
		for(int i = 0 ; i < n ; ++i)	cin >> num , v1.push_back(num);
		sort(v.begin(), v.end());
		sort(v1.begin(), v1.end());
		for(int i = 0 ; i < n ; ++i)	ans += (abs(v[i]-v1[i]));
		cout << "Case " << tc << ": " << ans << endl;
	}
	return 0;
}