#include <iostream>
#define min(a,b) (a<b?a:b)
using namespace std;
int dp[1001][2],pf[1001][2],n,m,x,y;
int main()
{
	int i,j;
	char t;
	cin>>n>>m>>x>>y;
	for (i=1;i<=n;i++)
		for (j=1;j<=m;j++)
		{
			cin>>t;
			if (t=='#')
				pf[j][0]++;
			else
				pf[j][1]++;
		}
	for (j=1;j<=m;j++)
	{
		pf[j][0]+=pf[j-1][0];
		pf[j][1]+=pf[j-1][1];
		dp[j][0]=dp[j][1]=1000000000;
	}
	dp[0][0]=0;
	dp[0][1]=0;
	for (i=0;i<=m;i++)
		for (j=x;j<=y;j++)
			if (i+j<=m)
			{
				dp[i+j][0]=min(dp[i+j][0],dp[i][1]+pf[i+j][0]-pf[i][0]);
				dp[i+j][1]=min(dp[i+j][1],dp[i][0]+pf[i+j][1]-pf[i][1]);
			}
	cout<<min(dp[m][0],dp[m][1]);
	return 0;
}
