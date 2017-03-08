#include<bits/stdc++.h>
using namespace std;
bool valid(string s)
{
	if(s.length()>16||s.size()==0)
		return 0;
	for(int i=0;i<s.length();i++)
		if(s[i]!='_'&&!isalpha(s[i])&&(s[i]<'0'||s[i]>'9'))
			return 0;
	return 1;
}
int main()
{
	string str; cin>>str;
	int at=str.find('@');
	if(at==-1)
		return cout<<"NO\n",0;
	string user=str.substr(0,at);
	if(!valid(user))
		return cout<<"NO\n",0;
	int r=str.find('/');
	string host;
	if(r!=-1)
	{
		string resoucre=str.substr(r+1);
		if(!valid(resoucre))
			return cout<<"NO\n",0;
		int len=r-at-1;
		host=str.substr(at+1,len);
	}
	else
		host=str.substr(at+1);
	if(host.length()==0||host.size()>32||host[host.size()-1]=='.')
		return cout<<"NO\n",0;
	stringstream ss(host);
	string t2sem;
	while(getline(ss,t2sem,'.'))
	{
		if(!valid(t2sem))
			return cout<<"NO\n",0;
	}
	cout<<"YES"<<endl;
	return 0;
}
