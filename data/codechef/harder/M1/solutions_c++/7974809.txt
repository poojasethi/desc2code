#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
 
#include <cmath>
#include <cstdio>
#include <queue>
#include <list>
#include <stack>
#include <utility>
#include <numeric>
#include <map>
#include <cctype>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <cassert>
#include <iomanip>
#include <set>
 
using namespace std;
 
#define F(a,b) for(int a=0;a<b;a++)
#define REP(a,b) for(int a=0;a<b;a++)
#define FOR(a,b,c) for(int a=b;a<c;a++)
#define FORD(a,b,c) for(int a=b;a>=c;a--)
 
#define S scanf
#define P printf
 
#define LEN(x) ((int)x.length())
#define SZ(x) ((int)x.size())
#define ALL(x) x.begin(), x.end()
#define MP(x,y) make_pair(x,y)
#define PB(x) push_back(x)
#define INF 1000000000
 
typedef long long LL;
typedef pair<int,int> PII;
typedef pair<int, PII> PIII;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<string> VS;
 
 
 
int dp[20][1<<20];
 
int dp1[20][1<<20];
 
bool possible[1<<20];
 
char A[25][25];
int mask[20];
 
void generate( int j, int n, int Num )
{
	if(j>=n)
	{
		possible[Num] = true;
		return;
	}
	generate( j+2, n, Num|(1<<(n-j-1)));
	generate( j+1, n, Num);
}
 
//void solve( int i, int j, int n, int Num, vector<VI> &dp, vector<VI> &dp1 )
void solve( int i, int j, int n, int Num)
{
	assert(possible[Num]);
	if(j>=n)
	{
		//G[i][GC[i]++] = Num;
		dp[i][Num] = 1;
		dp1[i][Num] = __builtin_popcount(Num);
		return;
	}
	if(A[i][j]!='*')
		solve( i, j+2, n, Num|(1<<(n-j-1)));
		//solve( i, j+2, n, Num|(1<<(n-j-1)), dp, dp1);
	//solve( i, j+1, n, Num, dp, dp1);
	solve( i, j+1, n, Num);
}
 
//inline void fill( int prev, int i, int n ,int bitmask, int Num, vector<VI> &dp, vector<VI> &dp1, int bc )
inline void fill( int prev, int i, int n ,int bitmask, int Num, int bc )
{
	if(dp[prev][Num])
	{
		int tmp = bc + dp1[prev][Num];
		if(tmp > dp1[prev+1][bitmask] )
		{
			dp1[prev+1][bitmask] = tmp;
			dp[prev+1][bitmask] = dp[prev][Num];
		}
		else if( tmp == dp1[prev+1][bitmask] )
		{
			dp[prev+1][bitmask] += dp[prev][Num];
			if( dp[prev+1][bitmask] >= 151109 )
				dp[prev+1][bitmask] -= 151109;
		}
	}
	FOR(x, i, n)
	{
		if( A[prev][x]!='*' &&  (bitmask&(Num|(1<<(n-1-x)))) == 0 )
		{
			//fill( prev
			//
			//, i+2, n, bitmask, Num|(1<<x), dp, dp1, bc );
			fill( prev, x+2, n, bitmask, Num|(1<<(n-1-x)), bc );
		}
	}
}
 
int main()
{
	generate( 0 , 20, 0 );
 
	int t;
	int n,m;
 
 
	S("%d",&t);
	while(t--)
	{
		//memset(dp,0,sizeof(dp));
		//memset(dp1,0,sizeof(dp1));
		//
 
		S("%d%d",&n,&m);
		REP(i,n) S("%s",A[i]);
 
		bool fl = true;
		REP(i,n) REP(j,m) if(A[i][j]=='*') fl = false;
 
		if(fl)
		{
			if( (n==1 || m==1) && (n%2==0 || m%2==0))
			{
				if(n==1)
				{
					P("%d %d\n",m*n/2, m/2+1);
				}
				else
				{
					P("%d %d\n",m*n/2, n/2+1);
				}
			}
			else if(n%2==0)
			{
				if(m%2==0)
					P("%d %d\n",(m*n)/2, 2 );
				else
					P("%d %d\n",m*n/2, 2);
			}
			else
			{
				if(m%2==0)
				{
					P("%d %d\n", (m/2)*n, 2 );
				}
				else
				{
					P("%d %d\n", ((m/2+1)*(n/2+1)) + ((m/2)*(n/2)), 1);
				}
			}
			continue;
		}
 
		//vector< VI > dp(n , VI(1<<m) );
		//vector< VI > dp1(n , VI(1<<m) );
 
		REP(xx, 1<<m) dp1[0][xx]=dp[0][xx]=0;
		solve( 0 , 0 , m, 0 );
		//solve( 0 , 0 , m, 0, dp, dp1 );
 
		REP(i,n)
		{
			mask[i] = 0;
			REP(j,m)
			{
				if(A[i][j]=='*') mask[i]|=(1<<(m-1-j));
			}
			//P("%d\n",mask[i]);
		}
 
 
		FOR(i,1,n)
		{
					FOR(j,0,1<<m)
					{
						dp[i][j]=dp1[i][j]=-1;
 
 
						if( (j&mask[i])==0 && possible[j] )
						{
							fill( i-1, 0, m, j, 0,  __builtin_popcount(j) );
						}
					}
		}
		int mval=-1, ans=-1;
		REP(i,1<<m)
		{
			if(dp1[n-1][i] > mval )
			{
				mval = dp1[n-1][i];
				ans = dp[n-1][i];
			}
			else if( dp1[n-1][i] == mval )
			{
				ans +=dp[n-1][i];
				if( ans >= 151109 ) ans-=151109;
			}
		}
		//assert(mval>1 && ans>=0 && ans<151109);
		P("%d %d\n",mval, (ans%151109+151109)%151109);
	}
	return 0;
}
 