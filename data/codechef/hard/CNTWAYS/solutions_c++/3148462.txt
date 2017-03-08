#include<cstdio>
#include<iostream>
#include<vector>
#include<cstring>
#include<algorithm>
#include<numeric>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<list>
#include<climits>
#include<cstdlib>
#include<string>
#include<cmath>

using namespace std;

// useful input/output macros
#define s(n) scanf("%d",&n)
#define sll(n) scanf("%lld",&n)
#define p(n) printf("%d\n",n)
#define pll(n) printf("%lld\n",n)
#define sf(n) scanf("%lf\n",&n)
#define pf(n) printf("%lf\n",n)

// useful functions
#define rev(s,e) reverse(s,e)
#define mset(s,i) memset(s,i,sizeof(s))
#define cpy(i,j) memset(i,j,sizeof(j))
#define mp(x,y) make_pair(x,y)
#define f(i,a,b) for(int i=a;i<b;i++)
#define fk(i,a,b,k) for(int i=a;i<b;i+=k)
#define fr(i,a,b) for(int i=a;i>b;i--)
#define frk(i,a,b,k) for(int i=a;i>b;i-=k)
#define pb(x) push_back(x)

// shortforms
#define ff first
#define ss second
#define ld long double
#define li long int
#define lli long long int
#define ug unsigned

// constants
const ld eps=1e-9;
const ld pi=3.141592653589793;
const ld e=2.718281828459045;


#define inf 1000000007

lli invfact[800010],fact[800010],inv[800010];

lli choose(int x,int y){
  return (((fact[x]*invfact[y])%inf)*invfact[x-y])%inf;
}

lli ways(int n,int m){
  return choose(n+m,m);
}

int main(){
  inv[1]=1;
  f(i,2,800010){
    inv[i]=inf -((inf/i)*inv[inf%i]%inf);
  }
  fact[0]=invfact[0]=1;
  f(i,1,800010){
    fact[i]=(fact[i-1]*i)%inf;
  }
  f(i,1,800010){
    invfact[i]=(invfact[i-1]*inv[i])%inf;
  }
  int t,n,m,a,b;
  lli res;
  s(t);
  while(t--){
    s(n);s(m);s(a);s(b);
    res=0;
    f(p,a,n+1){
      res+=ways(n-p,b-1)*ways(p,m-b);
      res%=inf;
    }
    p((int)res);
  }
}
