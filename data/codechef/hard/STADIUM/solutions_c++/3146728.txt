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
#define pii pair<int,int>

// constants
const int inf=1000000007;
const ld eps=1e-9;
const ld pi=3.141592653589793;
const ld e=2.718281828459045;

//jobs are stored in a pair indicating start time and end time

pii arr[100001];

int main(){
  int n,time,jobs;
  time=jobs=0;
  s(n);
  f(i,0,n){
    s(arr[i].ss);s(arr[i].ff);
    arr[i].ff+=arr[i].ss;
  }
  sort(arr,arr+n);
  f(i,0,n){
    if(arr[i].ss>time){
      time=arr[i].ff;
      jobs++;
    }
  }
  p(jobs);
}
