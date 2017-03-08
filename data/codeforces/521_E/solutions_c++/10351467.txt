#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<vector>
#include<map>
#include<cmath>
#include<queue>
#include<set>
#define PII pair<int,int>
#define f first
#define s second
#define VI vector<int>
#define LL long long
#define MP make_pair
#define LD long double
#define PB push_back
#define ALL(V) V.begin(),V.end()
#define abs(x) max((x),-(x))
#define PDD pair<LD,LD> 
#define VPII vector< PII > 
#define siz(V) ((int)V.size())
#define FOR(x, b, e)  for(int x=b;x<=(e);x++)
#define FORD(x, b, e) for(int x=b;x>=(e);x--)
#define REP(x, n)     for(int x=0;x<(n);x++)
#define mini(a,b) a=min(a,b)
#define maxi(a,b) a=max(a,b)
using namespace std;
int n,a,b,c,d,k,m,q,z;
VI V[200004];
int pop[200004];
VPII powrotne[200004];
int odw[200004];
int odl[200004];

VI idz(int a,int b)//a zawsze niżej niż b
  {
  if(odl[a]<odl[b])
    {
    puts("idz a wyżej niż b");
    exit(-1);
    }
  VI ret;
  ret.PB(a);
  while(a!=b)
    {
    a=pop[a];
    ret.PB(a);
    }
  return ret;
  }
void pisz(VI V)
  {
  printf("%d ",(int)V.size());
  REP(i,V.size())printf("%d ",V[i]);
  puts("");
  }
void koncz(PII a,PII b,int x)
  {
  if(odl[a.s]<odl[b.s])swap(a,b);
  //koniec a jest zawsze nizej/ta sama wysokosc
  int x1=a.f;
  int y1=a.s;
  int x2=b.f;
  int y2=b.s;
  VI s1=idz(x,y1);
  VI s2=idz(x1,x);
  reverse(ALL(s2));
  s2.PB(y1);
  
  VI s3=idz(x2,x);
  reverse(ALL(s3));
  VI temp=idz(y1,y2);
  reverse(ALL(temp));
  REP(i,temp.size())s3.PB(temp[i]);
  puts("YES");
  pisz(s1);
  pisz(s2);
  pisz(s3);
  exit(0);
  }
void dfs(int x)
  {
  odw[x]=1;
  REP(i,V[x].size())
    {
    if(V[x][i]==pop[x])continue;
    if(odw[V[x][i]])
      {
      if(odl[V[x][i]]<odl[x])
        {
        powrotne[x].PB(MP(x,V[x][i]));
        }
      continue;
      }
    odl[V[x][i]]=odl[x]+1;
    pop[V[x][i]]=x;
    dfs(V[x][i]);
    REP(j,powrotne[V[x][i]].size())
      {
      if(powrotne[V[x][i]][j].s!=x)powrotne[x].PB(powrotne[V[x][i]][j]);
      }
    }
  if(powrotne[x].size()>1)
    {
//    cerr<<x<<endl;
    koncz(powrotne[x][0],powrotne[x][1],x); 
    }
  }
main()
{
scanf("%d%d",&n,&m);
FOR(i,1,m)
  {
  scanf("%d%d",&a,&b);
  V[a].PB(b);
  V[b].PB(a);
  }
FOR(i,1,n)
  {
  if(odw[i]==0)dfs(i);
  }
puts("NO");
}
