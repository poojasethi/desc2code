#include<iostream>
using namespace std;
int dp[1024][1024];
int n;
int a[1024];
int solve (int p, int q)
{
  if (dp[p][q]) return dp[p][q];
  if (q == n) return dp[p][q] = a[p];
  if (q == n-1) return dp[p][q] = max(a[p], a[q]);
  dp[p][q] = min(solve(q+1, q+2) + max(a[p],a[q]), solve(p,q+2) + max(a[q],a[q+1]));
  dp[p][q] = min(dp[p][q], solve(q,q+2) + max(a[p], a[q+1]));
  return dp[p][q];
}
void printResults(int p, int q)
{
  if (q == n) cout<<p + 1<<endl;
  else if (q == n-1) cout<<p + 1<<" "<<q + 1<<endl;
  else {
    if (dp[p][q] == dp[q+1][q+2] + max(a[p], a[q])) {
      cout<<p + 1<<" "<<q + 1<<endl;
      printResults(q+1, q+2);
    } else if (dp[p][q] == dp[p][q+2] + max(a[q], a[q+1])) {
      cout<<q + 1<<" "<<q+1 + 1<<endl;
      printResults(p, q+2);
    } else {
      cout<<p + 1<<" "<<q+1 + 1<<endl;
      printResults(q, q+2);
    }
  }
}
int main()
{
  cin>>n;
  for (int i = 0; i < n; i++) cin>>a[i];
  cout<<solve(0,1)<<endl;
  printResults(0,1);
  return 0;
}
