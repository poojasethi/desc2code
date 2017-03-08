#include<iostream>
using namespace std;
int G[111][111];
int main()
{
  int k;
  cin>>k; k--;
  int n = 3;
  G[1][2] = G[2][1] = 1;
  G[2][3] = G[3][2] = 1;
  G[3][1] = G[1][3] = 1;
  while (k) {
    n++;
    G[1][n] = G[n][1] = 1;
    for (int i = 1; i < n-1 && i <= k; i++) {
      G[i+1][n] = G[n][i+1] = 1;
      k -= i;
    }
  }
  cout<<n<<endl;
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) cout<<G[i][j];
    cout<<endl;
  }
  return 0;
}
