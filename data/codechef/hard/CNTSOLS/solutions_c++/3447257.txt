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
const lli inf=1000000007; //prime 
const ld eps=1e-9;
const ld pi=3.141592653589793;
const ld e=2.718281828459045;

lli cnt[51];

lli mod_pow(lli x,lli y,lli k){
  if(y==0){
    return 1%k;
  }
  lli tmp=x,ans=1ll;
  for(;y;y>>=1){
    if(y&1){
      ans=(ans*tmp)%k;
    }
    tmp=(tmp*tmp)%k;
  }
  return ans;
}

int main(){
  int t,u,m,d,N,cr;
  lli answer;
  s(t);
  while(t--){
    s(u);s(d);s(m);s(N);
    mset(cnt,0);
    f(i,0,N){
      cr=mod_pow(i,d,N);
      if(i<=u){
	cnt[cr]+=(u-i)/N+1;
      }
    }
    answer=0;
    f(i,0,N){
      f(j,0,N){
	f(k,0,N){
	  if((i+j+k)%N==m%N){
	    answer+=(cnt[i]*((cnt[j]*cnt[k])%inf))%inf;
	    answer%=inf;
	  }
	}
      }
    }
    p(answer);
  }
}
