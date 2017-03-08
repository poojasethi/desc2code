#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <cmath>
#include <cstring>
#include <iostream>
#include <stack>
#include <deque>
#include <map>
#include <vector>
#include <utility>
#include <set>

#define MOD (1000000007)
#define MAXINT 1e9

using namespace std;
typedef long long int ll;

int a[1002][1002],ans[1002][1002];

void work(int x,int y,int k)
{
	int i,j,l;
	for(i=0;i<x;i++)
	{
		deque <int> d;
		for(j=0;j<k;j++)
		{
			if(d.empty() || a[i][d.back()]<=a[i][j])	d.push_back(j);
			else
			{
				while(!d.empty() && a[i][d.back()]>a[i][j])	d.pop_back();
				d.push_back(j);
			}
		}
		l=0;
		ans[l++][i]=a[i][d.front()];
		for(;j<y;j++)
		{
			if(!d.empty() && d.front()==j-k)	d.pop_front();
			if(d.empty() || a[i][d.back()]<=a[i][j])	d.push_back(j);
			else
			{
				while(!d.empty() && a[i][d.back()]>a[i][j])	d.pop_back();
				d.push_back(j);
			}	
			ans[l++][i]=a[i][d.front()];
		}
	}
}

int main()
{
	int n,k,i,j;
	scanf("%d%d",&n,&k);
	for(i=0;i<n;i++)	for(j=0;j<n;j++)	scanf("%d",&a[i][j]);
	work(n,n,k);
	for(i=0;i<n-k+1;i++)	for(j=0;j<n;j++)	a[i][j]=ans[i][j];
	work(n-k+1,n,k);
	for(i=0;i<n-k+1;i++)	
	{
		for(j=0;j<n-k+1;j++)
			printf("%d ",ans[i][j]);
		printf("\n");
	}
	return 0;
}