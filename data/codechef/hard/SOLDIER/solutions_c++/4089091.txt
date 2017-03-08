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
#define MAXI 100000
#define mod 1000000007

using namespace std;

typedef long long int ll;
typedef struct xx
{
	int type,quality,price;
}s;

s a[10000];
vector<pair<int,int> > list[10];
int min_money[10][1005];

int b_search(vector<pair<int,int> > v,int q)
{
	int s,e,m,ans=-1;
	s=0;
	e=v.size()-1;
	if(v[e].first<q)	return -1;
	while(s<=e)
	{
		m=(s+e)>>1;
		if(v[m].first<q)
			s=m+1;
		else
		{
			ans=m;
			e=m-1;
		}
	}
	return ans;
}

int main()
{
	int n,t,i,j,ans,q,min_quality,money_req;
	scanf("%d%d",&n,&t);
	for(i=1;i<=n;i++)
	{
		scanf("%d%d%d",&a[i].type,&a[i].price,&a[i].quality);
		list[a[i].type].push_back(make_pair(a[i].quality,a[i].price));
	}
	for(i=1;i<=6;i++)	sort(list[i].begin(),list[i].end());
	for(i=1;i<=6;i++)
	{
		if(list[i].size()==0)	continue;
		min_money[i][list[i].size()-1]=list[i][list[i].size()-1].second;
		for(j=list[i].size()-2;j>=0;j--)
		{
			min_money[i][j]=min(min_money[i][j+1],list[i][j].second);
		}
	}
	ans=0;
	for(i=1;i<=6;i++)	if(list[i].size()==0)	break;
	if(i<7)	
		printf("0\n");
	else{
	for(i=1;i<=n;i++)
	{
		money_req=a[i].price;
		min_quality=a[i].quality;
		for(j=1;j<=6;j++)
		{
			if(j==a[i].type || list[j].size()==0)	continue;
			q=b_search(list[j],min_quality);
			if(q==-1)	money_req+=MAXI;
			else		money_req+=min_money[j][q];
		}
		if(money_req<=t)
			ans=max(ans,min_quality);
	}
	printf("%d\n",ans);
	}
	return 0;
}