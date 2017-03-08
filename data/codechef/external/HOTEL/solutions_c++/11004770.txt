#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class opr
{
public:
	int type;
	int time;
};


bool comp(opr p, opr q)
{
	if(p.time<q.time)return true;
	else if(p.time==q.time&&p.type<q.type)return true;
	return false;
}

int main()
{
	int t;
	cin>>t;
	for(int test=0;test<t;test++)
	{
		int n;
		cin>>n;
		vector<opr> vec;
		vec.resize(2*n);
		for(int i=0;i<n;i++)
		{
			cin>>vec[i].time;
			vec[i].type=1;
		}
		for(int i=0;i<n;i++)
		{
			cin>>vec[i+n].time;
			vec[i+n].type=0;
		}
		sort(vec.begin(),vec.end(),comp);
		int count=0,maxcnt=-1;
		for(int i=0;i<vec.size();i++)
		{
			if(vec[i].type==1)count++;
			else count--;
			maxcnt=max(maxcnt,count);
		}
		cout<<maxcnt<<endl;
	}
}