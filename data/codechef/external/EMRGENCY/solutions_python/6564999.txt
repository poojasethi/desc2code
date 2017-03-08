#include <bits/stdc++.h>
using namespace std;
vector<long long int>v[100005];
vector<bool>visited(100005,false);
vector<long long int>cost(100005,0);
long long int num,n,m,x,y,mincost,sum;
inline long long int scan( )
{
long long int n = 0;
char c;
for( c = getchar_unlocked(); c==' ' || c=='\n' || c == '\t'; c = getchar_unlocked());
for( ; c > 0x2f && c < 0x3a; c = getchar_unlocked())
n = (n * 10) + (c & 0x0f);
return n;
}
void dfs(long long int u)
{
	visited[u]=true;
	mincost=min(mincost,cost[u]);
	for (vector<long long int>::iterator i = v[u].begin(); i != v[u].end(); ++i)
	{
		if(visited[*i]==false)
			dfs(*i);
	}
}
int main(int argc, char const *argv[])
{
	int t;
	t=scan();
	while(t--)
	{
		sum=0;
		n=scan(),m=scan();
		cost.clear();
		visited.clear();
		for(long long int i=0;i<n;i++)
		{
			num=scan();
			cost.push_back(num);
			v[i].clear();
			visited.push_back(false);
		}
		while(m--)
		{
			x=scan(),y=scan();
			if(x==y)
				continue;
			x--,y--;
			v[x].push_back(y);
			v[y].push_back(x);
		}
		for (long long int i = 0; i < n; ++i)
		{
			if(visited[i]==false)
			{
				mincost=10008;
				dfs(i);
				sum+=mincost;
			}
		}
		cout<<sum<<endl;
	}
	return 0;
}