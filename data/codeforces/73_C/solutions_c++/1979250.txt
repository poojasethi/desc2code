#include<iostream>
#include<string>
#include<cstring>
using namespace std;
const int oo = 1000000000;
int p[256][256];
int dp[101][256][102];
string s;
int k, n;
int main()
{
  cin>>s>>k;
  cin>>n;
  for (int i = 0; i < n; i++) {
    char a, b; int x;
    cin>>a>>b>>x;
    p[a][b] = x;
  }
  for (int i = 0; i <= 100; i++) for (int j = 0; j < 256; j++) for (int l = 0; l <=101; l++) dp[i][j][l] = -oo;
  dp[0][s[0]][0] = 0;
  for (int c = 'a'; c <= 'z'; c++) if (c != s[0])
    dp[0][c][1] = 0;
  for (int i = 0; i < s.size() - 1; i++)
    for (int c = 'a'; c <= 'z'; c++)
      for (int j = 0; j <= k; j++) 
	for (int l = 'a'; l <= 'z'; l++)
	  dp[i+1][l][j + (l != s[i+1])] = max(dp[i+1][l][j + (l != s[i+1])],
					      dp[i][c][j] + p[c][l]);

  int ans = -oo;
  for (int i = 'a'; i <= 'z'; i++) for (int j = 0; j <= k; j++) {
      ans = max(ans, dp[s.size()-1][i][j]);
    }
  if (ans <= -oo) ans = 0;
  cout<<ans<<endl;
  return 0;
}
