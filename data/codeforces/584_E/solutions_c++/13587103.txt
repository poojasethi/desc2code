#include<bits/stdc++.h>
using namespace std;

typedef long long LL;

const int maxn = 2010;
int p[maxn],s[maxn];
int id[maxn];
vector<pair<int,int> > out;

int dfs(int a[],int n)
{
	if(n == 1) return 0;
	int pos,res = 0;
	for(int i=1;i<=n;++i) 
		if(a[i] == n) 
		{
			pos = i;
			break;
		}
	res += n - pos;
	for(int i=pos+1;i<=n;++i)
	{
		if(a[i] <= pos)
		{
			out.push_back(make_pair(pos,i));
			swap(a[pos],a[i]);
			pos = i;
		}
	}
	return res+dfs(a,n-1);
}

int main()
{
	//freopen("test.txt","r",stdin);
	
	int n;
	scanf("%d",&n);

	for(int i=1;i<=n;++i) scanf("%d",p+i);
	for(int i=1;i<=n;++i) scanf("%d",s+i),id[s[i]]=i;
	for(int i=1;i<=n;++i) p[i] = id[p[i]];

	//for(int i=1;i<=n;++i) printf("%d ",p[i]);


	printf("%d\n",dfs(p,n));
	printf("%d\n",out.size());
	for(int i=0;i<out.size();++i) printf("%d %d\n",out[i].first,out[i].second);
	return 0;
}
