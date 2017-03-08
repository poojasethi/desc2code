#include<iostream>
using namespace std;
const int sz = 1<<23;
int dp[1<<24];
int a[sz];
int main()
{
  int n;
  cin>>n;
  for (int i = 0; i < sz; i++) dp[i] = -1;
  for (int i = 0; i < n; i++) {
    cin>>a[i];
    dp[(~a[i])&(sz-1)] = a[i];
  }
  for (int k = sz - 1; k; k--) if (~dp[k]) {
      for (int i = k; i; i -= (i&-i)) dp[k^(i&-i)] = dp[k];
    }
  for (int i = 0; i < n; i++)
    cout<<dp[a[i]]<<" ";
  cout<<endl;
  return 0;
}
