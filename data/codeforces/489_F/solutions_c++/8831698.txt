#include <iostream>
using namespace std;

int N,M;
long long dp[506][506], MOD;
int count[3],t[500];

int main()
{
	string tmp;
	cin >> N >> M >> MOD;
	for(int i=0;i<M;i++)
	{
		cin >> tmp;
		for(int j=0;j<N;j++)
			t[j]+=tmp[j]-'0';
	}
	for(int i=0;i<N;i++)
		count[t[i]]++;
	dp[count[0]+2][count[1]+2] = 1;
	
	for(int i=N+2;i>=2;i--)
		for(int j=N+2;j>=2;j--)
		{
			dp[i-2][j+2] = (dp[i-2][j+2] + dp[i][j]*(i-2)*(i-3)/2)%MOD;
			dp[i-1][j] = (dp[i-1][j] + dp[i][j]*(i-2)*(j-2))%MOD;
			dp[i][j-2] = (dp[i][j-2] + dp[i][j]*(j-2)*(j-3)/2)%MOD;
		}
	
	cout << dp[2][2] << endl;
	return 0;
}
