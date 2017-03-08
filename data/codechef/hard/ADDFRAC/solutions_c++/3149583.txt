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
const int inf=1000000007; //prime 
const ld eps=1e-9;
const ld pi=3.141592653589793;
const ld e=2.718281828459045;

#define MAX 100007

// returns gcd of a,b in logarithmic time
int gcd(int a, int b){
  int temp;
  while(b){
    temp=b;
    b=a%b;
    a=temp;
  }
  return a;
}

//s toring numerators and denominators and stack for looping back and forth
int num[100001],den[100001],st[100001];

// calculates and stores the numerator and denominator for each index in its own position
void answer(int n){
  st[n]=n;
  int x,y,z;
  fr(ind,n-1,0){
    z=ind+1;
    while(n-z+1){
      x=num[z];y=den[z];
      // if we can increase it further
      if((1.0*num[ind])/den[ind]<(1.0*(num[ind]+x))/(den[ind]+y)){
	num[ind]+=x;
	den[ind]+=y;
	z=st[z]+1;
      }
      else{
	st[ind]=z-1;
	break;
      }
    }
    if(z>n){
      st[ind]=n;
    }
  }
}

int main(){
  int t,n,g;
  s(t);
  while(t--){
    s(n);
    f(i,1,n+1){
      scanf("%d/%d",&num[i],&den[i]);
    }
    answer(n);
    f(i,1,n+1){
      g=gcd(num[i],den[i]);
      printf("%d/%d\n",num[i]/g,den[i]/g);
    }
    printf("\n");
  }
}
