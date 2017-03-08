#include<iostream>
#include<string>
using namespace std;
const int mod = 1e9+7;
int main()
{
  int k;
  string start, end;
  cin>>start>>end;
  cin>>k;
  int n = start.size();
  string word = start+start;
  long long dp[2] = {1, 0};
  for (int i = 1; i <= k; i++) {
    long long tmp = (dp[1]*(n-1) + mod)%mod;
    dp[1] = (dp[1]*(n-2) + dp[0] + mod)%mod;
    dp[0] = tmp;
  }
  long long ans = 0;
  for (int i = 0; i < n; i++) {
    bool ok = true;
    for (int j = i; j < i + n; j++) if (word[j] != end[j-i]) ok = false;
    if (ok)
      ans = (ans + dp[i!=0] + mod)%mod;
  }
  cout<<ans<<endl;
  return 0;
}

