#include <bits/stdc++.h>
using namespace std;
int main()
{
	int i,n,cnt=0;
	string s;
	cin >> n;
	cin >> s;
	for(i=0;i<n;i++)
	{
		cnt++;
		if(s[i]=='0')
			break;
	}
	cout << cnt;
	return 0;
}