#include <cstdio>
#include <stack>
#include <vector>
using namespace std;
#define ll long long 
ll i,u,v,n,m;
vector<ll> graph[10002];
bool dfs(vector<ll> graph[] ,ll u)
{
	bool nodevisited[n+1];
	stack<ll> s;
	for(i=0;i<n+1;i++)
	{
		nodevisited[i]=false;
	}
	s.push(u);
	ll temp,temp2,twograph_check=0;
	while(!s.empty())
	{	
		twograph_check++;
		temp=s.top();
		s.pop();
		if(nodevisited[temp])
		{
			return false;
		}
		else
		{
			nodevisited[temp]=true;
			for(i=0;i<graph[temp].size();i++)
			{
				temp2=graph[temp][i];
				s.push(temp2);
			}
		}
	}
	if(twograph_check!=n)
	{
		return false;
	}
	else
	{
		return true;
	}
}
int main()
{
	scanf("%lld %lld",&n,&m);
	for(i=0;i<m;i++)
	{
		scanf("%lld %lld",&u,&v);
		graph[u].push_back(v);
	}
	if(dfs(graph,1) && m+1==n)
	{
		printf("YES\n");
	}
	else
	{
		printf("NO\n");
	}
	return 0;
}