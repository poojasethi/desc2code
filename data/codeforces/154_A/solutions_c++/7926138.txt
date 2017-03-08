#include<iostream>
#include<cstdio>
using namespace std;
int n;
string s;
int ans;
int c, d;
string str;
int main()
{
	ios::sync_with_stdio(0);
	cin >> s >> n;
	for(int i = 1; i <= n; ++i)
	{
		cin >> str;
		char x = str[0], y = str[1]; 
		c = d = 0;
		for(int i = 0; i < s.length(); ++i)
		{
			if(s[i] != x && s[i] != y)
				ans += min(c, d), c = 0, d = 0;
			if(s[i] == x) ++c;
			if(s[i] == y) ++d;
		}	
		ans += min(c, d);
	}
	cout << ans;
}