#include <bits/stdc++.h>
using namespace std;
int main()
{
	int n,v,i,k,m,s;
	vector <int> ans;
	cin >> n >> v;
	for(i=1;i<=n;i++)
	{
		cin >> k;
		m=10000000;
		while(k--)
		{
			cin >> s;
			m=min(s,m);
		}
		if(m<v)
			ans.push_back(i);
	}
	int l=ans.size();
	cout << l << endl;
	for(i=0;i<l;i++)
		cout << ans[i] << " ";
		return 0;
}