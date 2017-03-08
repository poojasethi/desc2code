#include <iostream>
#include <string>
#include <map>
#include <stdio.h>
using namespace std;
int mnc[13]={0,31,28,31,30,31,30,31,31,30,31,30,31};
int strtoint(string s)
{
	int rec;
	sscanf(s.c_str(),"%d",&rec);
	return rec;
}
bool iscurrent(string s)
{
	int m=strtoint(s.substr(3,2)),d=strtoint(s.substr(0,2));
	return s[0]>='0'&&s[0]<='9'&&s[1]>='0'&&s[1]<='9'&&s[2]=='-'&&s[3]>='0'&&s[3]<='9'&&s[4]>='0'&&s[4]<='9'&&s[5]=='-'&&s[6]=='2'&&s[7]=='0'&&s[8]=='1'&&s[9]>='3'&&s[9]<='5'&&m>0&&m<=12&&d>0&&d<=mnc[m];
}
int main()
{
	int i,mx=0;
	string s,ans;
	map<string,int> mp;
	map<string,int>::iterator it;
	cin>>s;
	for (i=0;i<s.size()-10+1;i++)
		if (iscurrent(s.substr(i,10)))
			mp[s.substr(i,10)]++;
	for (it=mp.begin();it!=mp.end();it++)
		if (it->second>mx)
		{
			mx=it->second;
			ans=it->first;
		}
	cout<<ans;
	return 0;
}
