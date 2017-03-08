#include<stdio.h>
#include<algorithm>
#include<cstring>
#include<vector>
#include<map>
#include<set>
#define REP(i,b,e) for(int i=b; i<=e; i++)
#define RREP(i,b,e) for(int i=b; i>=e; i--)

using namespace std;
#define SZ 210
#define MOD 1000000007

int m,k;

int ch[SZ][20],sz,val[SZ];
void insert(int *num,int v)
{
  int u=0;
  REP(i,1,num[0])
  {
    if(!ch[u][num[i]])ch[u][num[i]]=++sz;
    u=ch[u][num[i]];
  }
  val[u]+=v;
}

int fa[SZ],fr,rr,q[SZ];
void calc_fa()
{
  fr=0,rr=-1;
  for(int i=0; i<m; i++)if(ch[0][i])q[++rr]=ch[0][i];
  while(fr<=rr)
  {
    int r=q[fr++];
    for(int i=0; i<m; i++)
    {
      int u=ch[r][i];
      if(!u){ch[r][i]=ch[fa[r]][i];continue;}
      fa[u]=ch[fa[r]][i];
      val[u]+=val[fa[u]];
      q[++rr]=u;
    }
  }
}

int d[SZ][SZ][510];
int dp(int u,int L,int v)
{
  if(v<0)return 0;
  if(L==0)return 1;
  if(d[u][L][v]!=-1)return d[u][L][v];
  d[u][L][v]=0;
  REP(i,0,m-1)
  {
    d[u][L][v]+=dp(ch[u][i],L-1,v-val[ch[u][i]]);
    d[u][L][v]%=MOD;
  }
  return d[u][L][v];
}
int calc(int *dig)
{
  int ret=0,u=0;
  for(int i=1; i<dig[0]; i++)
  {
    REP(j,1,m-1)
    {
      ret+=dp(ch[u][j],i-1,k-val[ch[u][j]]);
      ret%=MOD;
    }
  }
  int sum=0;
  for(int i=dig[0]; i; i--)
  {
    for(int j=(i==dig[0]?1:0); j<dig[i]; j++)
    {
      ret+=dp(ch[u][j],i-1,k-sum-val[ch[u][j]]);
      ret%=MOD;
    }
    u=ch[u][dig[i]];
    sum+=val[u];
    if(sum>k)break;
  }
  return (ret+(sum<=k))%MOD;
}

int l[SZ],r[SZ];

int n,num[SZ];
int main()
{

  scanf("%d%d%d",&n,&m,&k);
  scanf("%d",&l[0]);
  REP(i,1,l[0])scanf("%d",&l[i]);
  reverse(l+1,l+l[0]+1);
  scanf("%d",&r[0]);
  REP(i,1,r[0])scanf("%d",&r[i]);
  reverse(r+1,r+r[0]+1);
  REP(i,1,n){
    scanf("%d",&num[0]);
    REP(j,1,num[0])scanf("%d",&num[j]);
    int v;
    scanf("%d",&v);
    insert(num,v);
  }
  calc_fa();
  int tmp=0,u=0;
  RREP(i,l[0],1){
    u=ch[u][l[i]];
    tmp+=val[u];
  }
  memset(d,-1,sizeof(d));
  printf("%d",((calc(r)-calc(l)+(tmp<=k))%MOD+MOD)%MOD);
  return 0;
}