#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <cmath>

#define FOR(i,a,b) for(int i=a; i<b; i++)

using namespace std;

string s,t;

int n,m,dp[1100][1100];

void showHow(int i,int j)
{
	if(!(i || j))
		return;
	int b = (s[i-1] != t[j-1]);
	if(i && dp[i][j] == dp[i-1][j] + 1)
	{
		cout<<"DELETE "<<i<<endl;
		showHow(i-1,j);
	}
	else if ( j && dp[i][j] == dp[i][j-1] +1)
	{
		cout<<"INSERT "<<i+1<<" "<<t[j-1]<<endl;
		showHow(i,j-1);
	}
	else
	{
		if(b)
			cout<<"REPLACE "<<i<<" "<<t[j-1]<<endl;
		showHow(i-1,j-1);
	}
}

int main()
{
		cin>>s>>t;
		n = s.size();
		m = t.size();
		FOR(i,0,1001)
			dp[0][i] = dp[i][0] = i;
		FOR(i,1,n+1)
			FOR(j,1,m+1)
				dp[i][j] = min( 1 + min( dp[i][j-1] , dp[i-1][j] ) , (s[i-1] != t[j-1]) + dp[i-1][j-1] );
		cout<<dp[n][m]<<endl;
		showHow(n,m);
}
