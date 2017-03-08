#include <bits/stdc++.h>
using namespace std;
int main()
{
	int n,k,cnt=0,i;
	pair<int,int> a[103];
	vector<int> v;
	cin >> n >> k;
	for(i=1;i<=n;i++)
	{
		cin >> a[i].first;
		a[i].second=i;
	}
	sort(a,a+n);
	for(i=1;i<=n;i++)
	{
		if(k>=a[i].first)
		{
			cnt++;
			k-=a[i].first;
			v.push_back(a[i].second);
		}
	}
	cout << cnt << endl;
	for(i=0;i<cnt;i++)
		cout << v[i] << " ";
	return 0;
}