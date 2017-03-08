#include<bits/stdc++.h>
using namespace std;
int main()
{
	string s;
	cin>>s;
	int count = 1;
	for(int i=1;i<s.length();i++)
	{
		if(s[i]=='1')
		count+=10;
		else
		count += s[i] - '0';
	}
	cout<<count;
return 0;
}
