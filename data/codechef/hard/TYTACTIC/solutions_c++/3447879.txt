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

vector<int> graph[100010];
lli skill[100010],sum[500000];
int pre[100010],post[100010],lst[100010];
bool visited[100010];

int start_dfs(int vert,int time){
  pre[vert]=time;
  visited[vert]=true;
  int ret=time;
  f(i,0,graph[vert].size()){
    if(!visited[graph[vert][i]]){
      ret=start_dfs(graph[vert][i],ret+1);
    }
  }
  post[vert]=ret;
  return ret;
}

lli query(int bot,int top,int x,int y,int node){
  if(x>top || y<bot){
    return 0;
  }
  if(x<=bot && y>=top){
    return sum[node];
  }
  else{
    int mid=(top+bot)>>1;
    return query(bot,mid,x,y,2*node)+query(mid+1,top,x,y,2*node+1);
  }
}

void update(int bot,int top,int pos,int val,int node){
  int mid=(bot+top)>>1;
  if(bot==top && bot==pos){
    sum[node]=val;
  }
  else if(pos<=mid){
    update(bot,mid,pos,val,2*node);
    sum[node]=sum[2*node]+sum[2*node+1];
  }
  else{
    update(mid+1,top,pos,val,2*node+1);
    sum[node]=sum[2*node]+sum[2*node+1];
  }
}

void make_tree(int node,int bot,int top){
  int mid=(bot+top)>>1;
  if(bot==top){
    sum[node]=lst[bot];
  }
  else{
    make_tree(2*node,bot,mid);
    make_tree(2*node+1,mid+1,top);
    sum[node]=sum[2*node]+sum[2*node+1];
  }
}

int main(){
  mset(visited,false);
  int n,m;
  s(n);s(m);
  f(i,0,n){
    s(skill[i+1]);
  }
  int u,v;
  f(i,1,n){
    s(u);s(v);
    graph[u].pb(v);
    graph[v].pb(u);
  }
  start_dfs(1,1);
  f(i,1,n+1){
    lst[pre[i]]=skill[i];
  }
  make_tree(1,1,n);
  char t;
  int x,y;
  f(i,0,m){
    cin>>t;
    if(t=='Q'){
      s(x);
      p(query(1,n,pre[x],post[x],1));
    }
    else{
      s(x);s(y);
      update(1,n,pre[x],y,1);
    }
  }
}
