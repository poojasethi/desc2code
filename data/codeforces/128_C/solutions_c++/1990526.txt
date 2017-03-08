#include<iostream>
using namespace std;
const int mod = 1e9 + 7;
long long cr[1024][2048];
int main()
{
  for (int i = 0; i <= 1000; i++) {
    cr[i][0] = cr[i][i] = 1;
    for (int j = 1; j < i; j++)
      cr[i][j] = (cr[i-1][j-1] + cr[i-1][j])%mod;
  }
  int n, m, k;
  cin>>n>>m>>k;
  cout<<(cr[n-1][2*k]*cr[m-1][2*k])%mod<<endl;
  return 0;
}
