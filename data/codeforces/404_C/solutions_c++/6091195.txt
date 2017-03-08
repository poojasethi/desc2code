#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
const int maxn=100000+10;
pair<int,int> q[maxn];
int cnt[maxn];
vector< pair<int,int> > edges;
int main()
{
	int n,k;
	cin>>n>>k;
	for(int i=1;i<=n;i++)
	{
		cin>>q[i].first;
		q[i].second=i;
	}
	sort(q+1,q+n+1);
	int l=1,r=2;
	if(q[l].first!=0)
	{
		cout<<"-1"<<endl;
		return 0;
	}
	for(;r<=n;r++)
	{
		while(q[l].first<q[r].first-1||cnt[l]==k)
			l++;
		if(q[l].first==q[r].first)
		{
			cout<<"-1\n";
			return 0;
		}
		edges.push_back(make_pair(q[l].second,q[r].second));
		cnt[l]++;
		cnt[r]++;
	}
	cout<<edges.size()<<endl;
	for(int i=0;i<edges.size();i++)
		cout<<edges[i].first<<' '<<edges[i].second<<endl;
	return 0;
}
