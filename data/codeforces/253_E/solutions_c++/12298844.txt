#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
using namespace std;
struct task
{
	int t,s,p,ord;
	task(){}
	bool operator<(const task& b)const
	{
		if (t!=b.t)
			return t<b.t;
		return p<b.p;
	}
};
task tk[50001];
int n,ms,pgr[50001];
long long ans[50001];
long long check(int mp)
{
	int i;
	priority_queue<pair<int,int> > q;
	for (i=1;i<=n;i++)
		pgr[i]=tk[i].s;
	tk[ms].p=mp;
	for (i=1;i<=n;i++)
	{
		int cur;
		if (i==1)
			cur=0;
		else
			cur=tk[i-1].t;
		while (!q.empty()&&cur<tk[i].t)
		{
			pair<int,int> t=q.top();
			int pt=min(tk[i].t-cur,pgr[t.second]);
			pgr[t.second]-=pt;
			cur+=pt;
			if (!pgr[t.second])
			{
				ans[tk[t.second].ord]=cur;
				q.pop();
			}
		}
		q.push(make_pair(tk[i].p,i));
	}
	long long cur=tk[n].t;
	while (!q.empty())
	{
		pair<int,int> t=q.top();
		q.pop();
		cur+=pgr[t.second];
		ans[tk[t.second].ord]=cur;
	}
	return ans[tk[ms].ord];
}
int main()
{
	int i,l,r,m;
	long long res,t;
	vector<int> pos;
	set<int> pri;
#ifdef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif
	scanf("%d",&n);
	for (i=1;i<=n;i++)
	{
		scanf("%d%d%d",&tk[i].t,&tk[i].s,&tk[i].p);
		tk[i].ord=i;
		pri.insert(tk[i].p);
	}
	scanf("%I64d",&t);
	sort(tk+1,tk+n+1);
	for (i=1;i<=n;i++)
		if (tk[i].p==-1)
		{
			ms=i;
			break;
		}
	for (i=1;i<=n;i++)
		if (tk[i].p!=-1)
		{
			if (!pri.count(tk[i].p-1))
				pos.push_back(tk[i].p-1);
			if (!pri.count(tk[i].p+1))
				pos.push_back(tk[i].p+1);
		}
	sort(pos.begin(),pos.end());
	pos.resize(unique(pos.begin(),pos.end())-pos.begin());
	l=0;
	r=pos.size()-1;
	while (true)
	{
		m=(l+r)/2;
		res=check(pos[m]);
		if (res==t)
		{
			printf("%d\n",pos[m]);
			for (i=1;i<=n;i++)
				printf("%I64d ",ans[i]);
			return 0;
		}
		else if (res<t)
			r=m-1;
		else
			l=m+1;
	}
}
