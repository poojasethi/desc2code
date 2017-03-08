#include <iostream>
#include <sstream>
#include <vector>
#include <string>
using namespace std;
int mn[13]={0,31,29,31,30,31,30,31,31,30,31,30,31};
vector<int> v;
int strtoint(string s)
{
	stringstream ss;
	int ret;
	ss<<s;
	ss>>ret;
	return ret;
}
int main()
{
	string s;
	int idx=0,n,m;
	ios::sync_with_stdio(false);
	cin>>n>>m;
	getline(cin,s);
	while (getline(cin,s))
	{
		int mo=strtoint(s.substr(5,2));
		int d=strtoint(s.substr(8,2));
		int h=strtoint(s.substr(11,2));
		int mi=strtoint(s.substr(14,2));
		int se=strtoint(s.substr(17,2));
		int ln=((d*24+h)*60+mi)*60+se;
		int i;
		for (i=1;i<mo;i++)
			ln+=mn[i]*24*60*60;
		while (idx<(int)v.size()&&v[idx]+n<=ln)
			idx++;
		v.push_back(ln);
		if ((int)v.size()-idx>=m)
		{
			cout<<s.substr(0,19);
			return 0;
		}
	}
	cout<<-1;
	return 0;
}
