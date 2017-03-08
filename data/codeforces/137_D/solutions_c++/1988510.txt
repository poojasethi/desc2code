#include<iostream>
#include<cstring>
using namespace std;
const int oo = 1000000;
char s[512];
int c[512][512];
int memo[512][512];
int n;
void preprocess()
{
  n = strlen(s + 1);
  for (int i = 1; i <= n; i++) c[i][i] = 0;
  for (int l = 2; l <= n; l++)
    for (int i = 1; i + l - 1 <= n; i++) {
      int j = i + l - 1;
      c[i][j] = c[i+1][j-1] + (s[i] != s[j]);
    }
  memset(memo, -1, sizeof(memo));
}
int split[512][512];
int solve(int p, int k)
{
  if (p == n + 1) return 0;
  if (k == 0) return oo;
  if (~memo[p][k]) return memo[p][k];
  int &ret = memo[p][k];
  ret = oo;
  for (int i = p; i <= n; i++) {
    int t = c[p][i] + solve(i+1, k - 1);
    if (t < ret) {
      ret = t;
      split[p][k] = i + 1;
    }
  }
  return ret;
}

void print(int k)
{
  int p = 1;
  while (p <= n) {
    int i;
    for (i = p; i <= p + (split[p][k]-p)/2 - 1; i++)
      cout<<s[i];
    if ((split[p][k] - p)%2) cout<<s[i];
    for (i = p + (split[p][k]-p)/2 - 1; i >= p; i--)
      cout<<s[i];
    p = split[p][k];
    k--;
    if (p <= n) cout<<"+";
  }
  cout<<endl;
}

int main()
{
  int k;
  cin>>s+1;
  cin>>k;
  preprocess();
  cout<<solve(1, k)<<endl;
  print(k);
  return 0;
}
