#include <iostream>
#include <vector>
using namespace std;

unsigned long long ans=0,N;
vector<int> edges[80001];

long dfs(int cur, int p)
{
	vector<long long> sub;
	long long size=1, s;
	for(int i=0;i<edges[cur].size();i++)
	{
		if(edges[cur][i]==p)
			continue;
		s = dfs(edges[cur][i], cur);
		size += s;
		sub.push_back(s);
	}
	
	long long totp = size*(size-1)/2;
	for(int i=0;i<sub.size();i++)
		totp -= sub[i]*(sub[i]-1)/2;
	ans -= totp*totp;
	s = (N-size) * size;
	ans -= 2*s*totp;
	
	return size;
}

int main()
{
	cin >> N;
	
	ans = (N*(N-1)/2)*(N*(N-1)/2);
	//cout << ans << endl;
	
	int a,b;
	for(int i=0;i<N-1;i++)
	{
		cin >> a >> b;
		edges[a-1].push_back(b-1);
		edges[b-1].push_back(a-1);
	}
	
	dfs(0, -1);
	
	cout << ans << endl;
	return 0;
}

