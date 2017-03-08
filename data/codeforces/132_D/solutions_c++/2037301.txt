#include<iostream>
#include<string>
#include<sstream>
using namespace std;
string s;
int dp[1000001];
int len[1000001];
int main()
{
  cin>>s;
  for (int i = s.size()-1, l = 0; i >= 0; i--) {
    if (s[i] == '0') {
      if (s[i-1] != '0' && l >= 2) ++l, dp[i] = 1, len[i] = l;
      else l = 0, dp[i] = 0;
    } else {
      l++;
      if (l >= 2) dp[i] = 1, len[i] = l;
      else dp[i] = 0;
    }
  }
  int n = s.size();
  stringstream ss;
  int ans = 0;
  for (int i = 0; i < n; ) {
    if (dp[i]) {
      int k = len[i];
      ss<<"+2^"<<n-i<<endl;
      ss<<"-2^"<<n-i-k<<endl;
      ans += 2;
      while (k) {
	if (s[i] == '0') ss<<"-2^"<<n-i-1<<endl, ++ans;
	++i; --k;
      } 
    } else {
      if (s[i] == '1') ss<<"+2^"<<n-i-1<<endl, ++ans;
      ++i;
    }
  }
  cout<<ans<<endl;
  cout<<ss.str();
  return 0;
}
