#include <bits/stdc++.h>
using namespace std;
int main()
{
	int n,m,x,y;
	set <int> s;
	cin >> n >> m;
	while(n--)
	{
		cin >> x;
		while(x--)
		{
			cin >> y;
			s.insert(y);
		}
	}
	if(s.size()==m)
		cout << "YES";
	else
		cout << "NO";
	return 0;
}