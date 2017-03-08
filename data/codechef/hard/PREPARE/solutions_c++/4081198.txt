#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <cmath>
#include <cstring>
#include <iostream>
#include <stack>
#include <map>
#include <vector>
#define mod 1000000007

using namespace std;
typedef long long int ll;

pair<int,int >a[1003];
int d[1003][1003];
int sum[1003];

bool fun(pair<int,int> s,pair<int,int> t)
{
	return s.first>t.first;
}

int main()
{
	int test,n,x,y,ans,qr,le,i,j;
	scanf("%d",&test);
	while(test--)
	{
		for(i=0;i<=1000;i++)
			for(j=0;j<=1000;j++)	
				d[i][j]=0;
		scanf("%d",&n);
		for(i=1;i<=n;i++)
		{
			scanf("%d%d",&x,&y);
			a[i]=make_pair(x,y);
		}
		sort(a+1,a+n+1,fun);
		//for(i=1;i<=n;i++)	printf("%d %d\n",a[i].first,a[i].second);
		sum[0]=0;
		for(i=1;i<=n;i++)
			sum[i]=sum[i-1]+a[i].second;
		d[0][0]=1;
		for(i=1;i<=n;i++)
		{
			for(j=0;j<=1000;j++)
			{
				if(j-a[i].second<0)	d[i][j] = d[i-1][j];
				d[i][j] = d[i-1][j] || d[i-1][j-a[i].second];
			}
		}
		a[n+1]=make_pair(0,0);
		ans=10000;
		for(i=0;i<=n;i++)
		{
			for(j=0;j<=1000;j++)
			{
				if(d[i][j]==0)	continue;
				qr=max(j,sum[i]-j);
				le=max(qr,a[i+1].first);
				if(le<ans)	ans=le;
			}
		}
		printf("%d\n",ans);
	}
	return 0;
}