#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <cmath>

#define FOR(i,a,b) for(int i=a; i<b; i++)

using namespace std;

const int MAX = 1100;

int n,queue[MAX],dp[MAX][MAX];

void showHow(int i,int j)
{
	if(i>n)
		return;
	if(j>n)
	{
		cout<<i<<endl;
		return;
	}
	int x1x2,x1x3,x2x3;
	x1x2 = max(queue[i],queue[j]) + dp[j+1][j+2];
	x1x3 = max(queue[i],queue[j+1]) + dp[j][j+2];
	x2x3 = max(queue[j],queue[j+1]) + dp[i][j+2];
	if(dp[i][j] == x1x2)
	{
		cout<<i<<" "<<j<<endl;
		return showHow(j+1,j+2);
	}
	else if(dp[i][j] == x1x3)
	{
		cout<<i<<" "<<j+1<<endl;
		return showHow(j,j+2);
	}
	else
	{
		cout<<j<<" "<<j+1<<endl;
		return showHow(i,j+2);
	}
}


int main()
{
	cin>>n;
	FOR(i,1,n+1)
		scanf("%d",&queue[i]);
	FOR(i,1,n+1)
		dp[i][n+1] = dp[i][n+2] = queue[i];
	for(int i=n; i>=1; i--)
		for(int j=n;j>i;j--)
		{
			int x1x2,x1x3,x2x3;
			x1x2 = max(queue[i],queue[j]) + dp[j+1][j+2];
			x1x3 = max(queue[i],queue[j+1]) + dp[j][j+2];
			x2x3 = max(queue[j],queue[j+1]) + dp[i][j+2];
			dp[i][j] = min(x1x2,min(x2x3,x1x3));
		}
	cout<<dp[1][2]<<endl;
	showHow(1,2);
}
