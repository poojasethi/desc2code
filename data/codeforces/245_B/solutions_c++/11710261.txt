#include <iostream>
#include <string>
using namespace std;
int main()
{
	string s,t;
	cin>>s;
	if (s[0]=='h')
	{
		t+="http://";
		s=s.substr(4);
	}
	else
	{
		t+="ftp://";
		s=s.substr(3);
	}
	t+=s.substr(0,s.find("ru",1))+".ru";
	s=s.substr(s.find("ru",1)+2);
	if (s!="")
		t+="/"+s;
	cout<<t;
	return 0;
}
