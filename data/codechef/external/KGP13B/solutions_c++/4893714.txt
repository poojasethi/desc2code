# include <cstdio>
# include <cstdlib>
# include <algorithm>
# include <queue>
# include <cmath>
# include <cstring>
# include <iostream>
# include <stack>
# include <map>
# include <vector>
# include <utility>
# include <set>
# include <deque>

# define MOD (1000000007)
# define MAXINT 1e9

using namespace std;
typedef long long int ll;
vector<pair<int,int> > list;
int event[1000];
vector<pair<int,pair<int,int> > > a;

int main()
{
	int test,p,k,m,i,j,x,y,q,z,events,countries,ans;
	cin>>test;
	p=test;
	while(test--)
	{
		list.clear();
		a.clear();
		list.push_back(make_pair(0,0));
		cin>>events>>countries;
		for(i=1;i<=events;i++)	event[i]=0;
		for(i=1;i<=events;i++)
		{
			cin>>x>>y;
			list.push_back(make_pair(x,y));
		}
		for(i=1;i<=countries;i++)
		{
			cin>>z;
			for(j=1;j<=z;j++)
			{
				cin>>x>>y;
				event[x]+=y;
			}
		}
		for(i=1;i<=events;i++)
		{
			a.push_back(make_pair(list[i].first,make_pair(0,event[i])));
			a.push_back(make_pair(list[i].second,make_pair(1,-event[i])));
		}
		sort(a.begin(),a.end());
		q=0;
		ans=0;
		for(i=0;i<events*2;i++)
		{
			q=q+a[i].second.second;
			ans=max(q,ans);
		}
		cout<<"Case "<<p-test<<": "<<ans<<endl;
	}
}