#include<iostream>
#include<stdio.h>
using namespace std;
typedef long long ll;


ll power(ll x, ll n, int mod)
{
  x = x%mod;
  ll y = 1;
  while(n>0)
  {
    if(n&1) y = (y*x)%mod;
    x = (x*x)%mod;
    n>>=1;
  }
  return y;
}

int main()
{
  int t;
  ll n,k,mod = 1000000007;
  cin>>t;
  while(t--)
  {
    cin>>k>>n;
    if(n==1)
      puts("1");
    else if(n==2 || n==3)
      printf("%lld\n",k);
    else
    {
      ll factor = power(2,n-3,mod-1);
      ll ans = power(k,factor,mod);
      cout<<ans<<endl;
    }
  }

  return 0;
}
