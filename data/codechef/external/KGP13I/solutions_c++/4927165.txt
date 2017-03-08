# include <cstdio>
# include <cstdlib>
# include <algorithm>
# include <queue>
# include <cmath>
# include <cstring>
# include <iostream>
# include <stack>
# include <map>
# include <vector>
# include <utility>
# include <set>
# include <deque>

# define MOD (1000000007)
# define MAXINT 1e9

using namespace std;
typedef long long int ll;

char a[102],b[102];
int dp[102][102][105];

//dp[i][j][0] is the answer for i,j. 
//dp[i][j][1] is the answer if the last move was replace/nothing.
//dp[i][j][2] is the answer if the last move was deletion.
//dp[i][j][3]...dp[i][j][103] is the answer if the last move was insertion of (i-2) characters.

int main()
{
	int test,z,n,m,x,y,i,j,k;
	cin>>test;
	for(z=1;z<=test;z++)
	{
		for(i=0;i<=100;i++)	for(j=0;j<=100;j++)	for(k=0;k<=104;k++)	dp[i][j][k]=MAXINT;
		//cout<<dp[0][0][0];
		cin>>n>>m;
		cin>>a;
		cin>>b;
		cin>>x>>y;
		dp[0][0][0]=0;
		for(i=1;i<=n;i++)
			dp[i][0][0]=dp[i][0][2]=x+i;
		for(i=1;i<=m;i++)
			dp[0][i][0]=dp[0][i][2+i]=min(x+i,y);
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=m;j++)
			{
				if(a[i-1]==b[j-1])
					dp[i][j][1]=dp[i-1][j-1][0];
				else
					dp[i][j][1]=dp[i-1][j-1][0]+1;
				dp[i][j][0]=min(dp[i][j][0],dp[i][j][1]);
				dp[i][j][2]=min(dp[i-1][j][0]+x+1,dp[i-1][j][2]+1);
				dp[i][j][0]=min(dp[i][j][0],dp[i][j][2]);
				dp[i][j][3]=dp[i][j-1][0]+x+1;
				dp[i][j][0]=min(dp[i][j][0],dp[i][j][3]);
				for(k=2;k<=j;k++)
				{
					dp[i][j][k+2]=dp[i][j-1][k+1] + (k>(y-x) ? 0:1);
					dp[i][j][0]=min(dp[i][j][0],dp[i][j][k+2]);
				}
			}
		}
		cout<<"Case "<<z<<": ";
		cout<<dp[n][m][0]<<endl;
	}
	return 0;
}