#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<map>
#include<set>
#include<vector>
#include<queue>
#include<string>
#define REP(i,n) for(int i=0; i<n; i++)
#define FOR(i,n) for(int i=1; i<=n; i++)

typedef long long LL;
using namespace std;

typedef pair<int,int> pii;
#define MP make_pair

#define N 200010
#define LO 20

int x[N],y[N],xn,yn;

#define mid ((l+r)>>1)
#define lc (o<<1)
#define rc (o<<1|1)
#define INF (1<<30)
pii minv[N<<2];
set<pii> st[N<<2];

void modify(int o,int l,int r,int p,pii v,int del){
  if(l==r){
    if(del)
      st[o].erase(v);
    else
      st[o].insert(v);
    
    if(st[o].empty())
      minv[o]=MP(INF,0);
    else
      minv[o]=*st[o].begin();
    
    return;
  }
  if(p<=mid)modify(lc,l,mid,p,v,del);
  else modify(rc,mid+1,r,p,v,del);
  minv[o]=min(minv[lc],minv[rc]);
}
pii query(int o,int l,int r,int R){
  if(r<=R)
    return minv[o];
  if(R<=mid)return query(lc,l,mid,R);
  else return min(minv[lc],query(rc,mid+1,r,R));
}

int n;
int a[N],b[N],c[N],d[N];

queue<int> Q;
int dis[N],pre[N];
void bfs(){
  c[0]=d[0]=1;
  Q.push(0);
  while(!Q.empty()){
    int u=Q.front(),ut;
    pii tmp;
    if((tmp=query(1,1,xn,c[u])).first<=d[u]){
      ut=tmp.second;
      modify(1,1,xn,a[ut],tmp,1);
      Q.push(ut);
      dis[ut]=dis[u]+1;
      pre[ut]=u;
    }else
      Q.pop();
  }
}

int main(){
#ifdef QWERTIER
  freopen("in.txt","r",stdin);
#endif 
  scanf("%d",&n);
  memset(minv,0x3f,sizeof(minv));
  FOR(i,n){
    scanf("%d%d%d%d",&a[i],&b[i],&c[i],&d[i]);
    x[++xn]=a[i];
    x[++xn]=c[i];
    y[++yn]=b[i];
    y[++yn]=d[i];
  }
  x[++xn]=0;
  y[++yn]=0;
  sort(x+1,x+xn+1);
  xn=unique(x+1,x+xn+1)-x-1;
  sort(y+1,y+yn+1);
  yn=unique(y+1,y+yn+1)-y-1;
  FOR(i,n){
    a[i]=lower_bound(x+1,x+xn+1,a[i])-x;
    c[i]=lower_bound(x+1,x+xn+1,c[i])-x;
    b[i]=lower_bound(y+1,y+yn+1,b[i])-y;
    d[i]=lower_bound(y+1,y+yn+1,d[i])-y;
  }
  FOR(i,n)
    modify(1,1,xn,a[i],MP(b[i],i),0);
  bfs();
  if(dis[n]){
    printf("%d\n",dis[n]);
    int cur=n;
    vector<int> ans;
    while(cur){
      ans.push_back(cur);
      cur=pre[cur];
    }
    for(int i=ans.size()-1; i>=0; i--)
      printf("%d ",ans[i]);
  }else
    printf("-1\n");
  return 0;
}
  
