#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <stdio.h>
#include <vector>
using namespace std;
map<string,int> mps;
vector<pair<int,string> > v;
int main()
{
	string my,t,t1,t2;
	int n,i,val;
	map<string,int>::iterator it;
	cin>>my;
	cin>>n;
	getchar();
	for (i=1;i<=n;i++)
	{
		getline(cin,t);
		t1=t.substr(0,t.find_first_of(" "));
		if (t.substr(t.size()-4)=="wall")
		{
			t2=t.substr(t.find(" on ")+4,t.find("'s")-t.find(" on ")-4);
			val=15;
		}
		else if (t.find(" commented ")!=-1)
		{
			t2=t.substr(t.find(" on ")+4,t.find("'s")-t.find(" on ")-4);
			val=10;
		}
		else
		{
			t2=t.substr(t.find(" likes ")+7,t.find("'s")-t.find(" likes ")-7);
			val=5;
		}
		if (t1==my||t2==my)
		{
			mps[t1]+=val;
			mps[t2]+=val;
		}
		else
		{
			if (mps[t1]==0)
				mps[t1]=0;
			if (mps[t2]==0)
				mps[t2]=0;
		}
	}
	for (it=mps.begin();it!=mps.end();it++)
		if (it->first!=my)
			v.push_back(make_pair(-it->second,it->first));
	sort(v.begin(),v.end());
	for (i=0;i<v.size();i++)
		cout<<v[i].second<<endl;
	return 0;
}
