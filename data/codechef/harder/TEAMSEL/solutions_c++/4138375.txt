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

using namespace std;
typedef long long int ll;

int a[110];
ll dp[45005];

int main()
{
	int test,n,i,j,q,t1,t2,tot,k;
	cin>>test;
	while(test--)
	{
		cin>>n;
		tot=0;
		for(i=0;i<n;i++)
		{
			cin>>a[i];
			tot+=a[i];
		}
		if(n%2)	a[n++]=0;
		for(i=0;i<=tot;i++)
			dp[i]=0;
		dp[0]=1;
		for(i=0;i<n;i++)
		{
			for(j=tot;j>=0;j--)
			{
				q=j-a[i];
				if(0<=q && q<=tot)
				{
					dp[j]|=(dp[q]<<1);
				}
			}
		}
		t1=0;t2=tot;
		ll x=(((ll)1)<<(n/2));
		for(i=0;i<=tot/2;i++)
		{
			if(dp[i]&x)
				t1=i;
		}
		t2=tot-t1;
		printf("%d %d\n",t1,t2);
	}
	return 0;
}