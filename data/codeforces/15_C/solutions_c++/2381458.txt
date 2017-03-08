#include<iostream>
using namespace std;
typedef long long ll;
ll xorSum(ll x)
{
  switch(x%4) {
  case 0: return x;
  case 1: return 1;
  case 2: return x+1;
  case 3: return 0;
  }
  return 0;
}
int main()
{
  int n;
  cin>>n;
  ll ans = 0;
  for (int i = 0; i < n; i++) {
    ll x, m;
    cin>>x>>m;
    ans ^= xorSum(x+m-1)^xorSum(x-1);
  }
  if (ans) cout<<"tolik"<<endl;
  else cout<<"bolik"<<endl;
  return 0;
}
