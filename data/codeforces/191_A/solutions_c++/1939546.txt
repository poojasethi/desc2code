#include<iostream>
#include<string>
using namespace std;

int dp[26][26];

int main()
{
  int n;
  cin>>n;
  for (int i = 0; i < n; i++) {
    string name;
    cin>>name;
    int f = name[0] - 'a';
    int l = name[name.size() - 1] - 'a';
    for (int i = 0; i < 26; i++) if (dp[i][f]) {
	dp[i][l] = max(dp[i][l], dp[i][f] + (int)name.size());
      }
    dp[f][l] = max(dp[f][l], (int)name.size());
  }
  int ans = 0;
  for (int i = 0; i < 26; i++) ans = max(ans, dp[i][i]);
  cout<<ans<<endl;
  return 0;
}
