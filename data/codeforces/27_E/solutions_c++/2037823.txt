#include<iostream>
using namespace std;
int p[10] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
long long ans = 1000000000000000001ll;
int N;
void solve(int i, long long x, int n)
{
  if (n > N) return;
  if (n == N) ans = x;
  for (int j = 1; j <= 60; j++) {
    if (ans/p[i] < x) break;
    solve(i + 1, x*=p[i], n*(j+1));
  }    
}
int main()
{
  cin>>N;
  solve(0, 1, 1);
  cout<<ans<<endl;
  return 0;
}
