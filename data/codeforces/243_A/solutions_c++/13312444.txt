#include <bits/stdc++.h>
using namespace std ;
int main()
{
	long long int n,temp;
	set<long long int>ans;
	set<long long int> st;
	cin >> n;
	while(n--)
	{
		cin>>temp;
		set<long long int> use;
		use.insert(temp);
		for(set<long long int>::iterator i=st.begin();i!=st.end();i++)
		{
			use.insert(*i|temp);
		}
		st=use;
		ans.insert(use.begin(),use.end());
	}
	cout << ans.size() << "\n";
	return 0;
}