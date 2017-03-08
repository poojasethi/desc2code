#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;
#define N 2007
typedef long long ll;
const ll mod=1e9+7;
ll p[N][N];
ll sum[N];
char s[N];
int main()
{
  int n,k;
  scanf("%d%d%s",&n,&k,s);
  sum[0]=p[0][0]=1;
  ll c=1;
  ll cnt(0);
  for(int i=1;i<=n;++i)
    {
      ll li=s[i-1]-'a';
      ll mi='z'-s[i-1];
      for(int j=0;j<=k;++j)
	{
	  p[i][j]=(p[i][j]+sum[j]*li)%mod;
	  for(int l=i-1;l>=0 && (i-l)*(n-i+1)<=j;--l)
	    {
	      p[i][j]=(p[i][j]+mi*p[l][j-(i-l)*(n-i+1)])%mod,++cnt;
	    }
	}
      for(int j=0;j<=k;++j)
	sum[j]=(sum[j]+p[i][j])%mod;
    }
  ll ans(0);
  for(int i=0;i<=n;++i)
    ans=(ans+p[i][k])%mod;
  printf("%d",(int)ans);
  return 0;
}
