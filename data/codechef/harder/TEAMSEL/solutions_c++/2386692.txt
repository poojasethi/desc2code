#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
#define ll long long
#define getint(n) scanf("%d",&n)
ll dp[100][45000];
int main()
{
	int t,n,a[100],sum,sum1;
	ll one = 1;
	getint(t);
	while(t--)
	{
		getint(n);
		sum = 0;
		for(int i = 0 ; i<n ; i++)
		{
			getint(a[i]);
			sum += a[i];
		}
		dp[t][0] = 1;		
	
		for(int i = 0 ; i<n ; i++)
		{
			for(int j = sum/2 ; j >= a[i] ; j--)
			{
				dp[t][j] = dp[t][j] | (dp[t][j-a[i]]<<1);
			}
		}
	
		for(int i = sum/2 ; i>=0 ; i--)	
		{
			if( dp[t][i] & (one <<  n/2) || dp[t][i] & (one << ((n+1)/2)))
			{
				sum1 = i;
				break;
			}
		}
		sum -= sum1;

		if(sum > sum1)
			printf("%d %d",sum1,sum);
		else
			printf("%d %d",sum,sum1);
		if(t > 0)
			printf("\n\n");
		else
			printf("\n");
	}
	return 0;
}
