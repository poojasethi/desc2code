#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <ctime>

using namespace std;
typedef long long LL;
#define FOR(k,a,b) for(int k(a); k < (b); ++k)
#define FORD(k,a,b) for(int k(a-1); k >= (b); --k)
#define REP(k,a) for(int k=0; k < (a); ++k)
#define REPD(k,a) for(int k=(a-1); k >=0; --k)

vector<vector<int> > dp(501,vector<int> (501));

pair<int,int> calc(const vector<vector<int> >& v, int k)
{
	REP(i,k)
	REP(j,min(i+1,k-i+1))
	{
		dp[i][j]=0;
		if(i)
		{
			dp[i][j]=dp[i-1][j];
			if(j && dp[i][j]<dp[i-1][j-1])
				dp[i][j]=dp[i-1][j-1];
			if(j+1<k && dp[i][j]<dp[i-1][j+1])
				dp[i][j]=dp[i-1][j+1];
		}
		dp[i][j]+=v[i][j];
	}
	return make_pair(dp[k-2][0],dp[k-1][0]);
}

pair<int,int> calc2(const vector<vector<int> >& v, int N)
{
	REPD(j,N)
	FORD(i,N,max(N-j,j)-1)
	{
		dp[i][j]=0;
		if(j<N-1)
		{
			
			dp[i][j]=dp[i][j+1];
			if(i && dp[i][j]<dp[i-1][j+1])
				dp[i][j]=dp[i-1][j+1];
			if(i+1<N && dp[i][j]<dp[i+1][j+1])
				dp[i][j]=dp[i+1][j+1];
		}
		dp[i][j]+=v[i][j];
	}
	return make_pair(dp[N-1][1],dp[N-1][0]);
}

int main()
{
	int T,N;
	cin >> T;
	vector<vector <int> > v(501,vector<int> (501));
	REP(testCase,T)
	{
		cin >> N ;
		REP(i,N)
		REP(j,i+1)
		scanf("%d", &v[i][j]);
		pair<int,int> a,b;
		a=calc(v,N);
		b=calc2(v,N);
		cout << max(a.first+b.second,a.second+b.first) << endl;
	}
	return 0;
}
