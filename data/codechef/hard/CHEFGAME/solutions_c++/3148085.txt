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
const int inf=7+1e9;
const ld eps=1e-9;
const ld pi=3.141592653589793;
const ld e=2.718281828459045;


// we take mod with respect to this
const lli MAX=747474747;

//store the graph in graph and vertices in vt
int vt[6667][6];
lli graph[6667][6667];

// return square of the distance, we can compare this without taking the square root
lli sqd(int x,int y,int d){
  lli ans=0;
  f(i,0,d){
    ans+=1ll*(vt[x][i]-vt[y][i])*(vt[x][i]-vt[y][i]);
  }
  return ans;
}

// store the current distance and the fact that they are included/not
bool included[6667];
lli cdist[6667];


// returns the current farthest vertex not included in the MST
int farthestVertex(int n){
  int ans;
  lli dist=-1;
  f(i,0,n){
    if(cdist[i]>dist && !included[i]){
      dist=cdist[i];
      ans=i;
    }
  }
  return ans;
}

void recalculateDistances(int v,int n,int d){
  lli temp;
  f(i,0,n){
    temp=graph[v][i];
    if(temp>cdist[i]){
      cdist[i]=temp;
    }
  }
}

int main(){
  int t,n,d,v;
  lli ans;
  s(t);
  while(t--){
    //set all vertices to not included and current distance -1, ans=1
    mset(included,false);
    mset(cdist,-1);
    ans=1ll;

    // input the graph
    s(n);s(d);
    f(i,0,n){
      f(j,0,d){
	s(vt[i][j]);
      }
    }

    //calculate the distances
    f(i,0,n){
      f(j,0,n){
	if(j>i){
	  graph[i][j]=sqd(i,j,d);
	}
	else if(i==j){
	  graph[i][j]=0;
	}
	else{
	  graph[i][j]=graph[j][i];
	}
      }
    }

    // prims algo starts here
    if(n!=1){
      included[0]=true;
      recalculateDistances(0,n,d);
      f(i,0,n-1){
	v=farthestVertex(n);
	if(cdist[v]==0){
	  break;
	}
	included[v]=true;
	ans=(ans*(cdist[v]%MAX))%MAX;
	recalculateDistances(v,n,d);
      }
    }
    cout<<ans<<endl;
  }
}
