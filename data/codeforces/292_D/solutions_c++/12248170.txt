#include <stdio.h>
#include <string.h>
#include <vector>
using namespace std;
int n,m,k,l,r;
vector<pair<int,int> > nb[501];
bool vst[501];
void dfs(int k)
{
	int i;
	vst[k]=true;
	for (i=0;i<nb[k].size();i++)
		if ((nb[k][i].second<l||nb[k][i].second>r)&&!vst[nb[k][i].first])
			dfs(nb[k][i].first);
}
int main()
{
	int i,j,cnt,t1,t2;
	scanf("%d%d",&n,&m);
	for (i=1;i<=m;i++)
	{
		scanf("%d%d",&t1,&t2);
		nb[t1].push_back(make_pair(t2,i));
		nb[t2].push_back(make_pair(t1,i));
	}
	scanf("%d",&k);
	for (i=1;i<=k;i++)
	{
		cnt=0;
		scanf("%d%d",&l,&r);
		memset(vst,false,sizeof(vst));
		for (j=1;j<=n;j++)
			if (!vst[j])
			{
				dfs(j);
				cnt++;
			}
		printf("%d\n",cnt);
	}
	return 0;
}
