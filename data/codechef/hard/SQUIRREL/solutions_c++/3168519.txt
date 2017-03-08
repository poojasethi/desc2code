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
const int inf=2000000007;
const ld eps=1e-9;
const ld pi=3.141592653589793;
const ld e=2.718281828459045;

#define MAX 10010

int txt,n,m,k,mx,t[MAX],p[MAX],nut[MAX];
lli tot;

// checks if we can gather the required number in time 
bool satisfy(int time){
  tot=0;
  f(i,0,m){
    if(t[i]<=time){
      nut[i]=(time-t[i])/p[i] +1;
    }
    else{
      nut[i]=0;
    }
  }
  nth_element(nut,nut+m-n,nut+m);
  f(i,m-n,m){
    tot+=nut[i];
  }
  return tot>=k;
}

// returns the smallest time in which we can gather the required number
int smtime(int bot,int top){
  int mid;
  while(bot<top){
    mid=(bot+top)>>1;
    if(satisfy(mid)){
      top=mid;
    }
    else{
      bot=mid+1;
    }
  }
  return top;
}

int main(){
  s(txt);
  while(txt--){
    s(m);s(n);s(k);
    n=min(n,m);
    f(i,0,m){
      s(t[i]);
    }
    f(i,0,m){
      s(p[i]);
    }
    mx=inf;
    f(i,0,m){
      mx=min(k*p[i]+t[i],mx);
    }
    p(smtime(0,mx));
  }
}
