#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int maxn=2222;
char a[maxn][maxn];
int u[maxn][maxn],d[maxn][maxn],x[maxn],y[maxn],fin[maxn],qu[maxn],qd[maxn];
int i,j,n,m,last,lu,ru,ld,rd,ans,k;
void update(int j)
{
 for (int i=1;i<=n;i++)
 if (a[i][j]=='X')u[i][j]=0;
  else u[i][j]=u[i-1][j]+1;
 for (int i=n;i>=1;i--)
 if (a[i][j]=='X')d[i][j]=0;
  else d[i][j]=d[i+1][j]+1;
}
void dp(int x)
{
 lu=1;
 ru=0;
 ld=1;
 rd=0;
 last=0;
 for (int i=1;i<=m;i++)
 {
  while ((lu<=ru)&&(u[x][i]<=u[x][qu[ru]]))ru--;
  qu[++ru]=i;
  while ((ld<=rd)&&(d[x][i]<=d[x][qd[rd]]))rd--;
  qd[++rd]=i;
  if (a[x][i]!='X')
  {
   while (u[x][qu[lu]]+d[x][qd[ld]]-1<i-last)
   {
    ans=max(ans,u[x][qu[lu]]+d[x][qd[ld]]-1);
    if (qu[lu]<qd[ld])
    {
     last=qu[lu];
     lu++;
    }
    else
    {
     last=qd[ld];
     ld++;
    }
   }
  ans=max(ans,i-last);
  }
}   
}
int main()
{
 scanf("%d %d %d\n",&n,&m,&k);
 for (i=1;i<=n;i++)
  for (j=1;j<=m;j++)
   {
    a[i][j]=getchar();
    while ((a[i][j]!='X')&&(a[i][j]!='.'))a[i][j]=getchar();
   }
 for (i=1;i<=k;i++)scanf("%d %d\n",&x[i],&y[i]);
 ans=0;
 for (i=1;i<=k;i++)a[x[i]][y[i]]='X';
 memset(u,0,sizeof(u));
 memset(d,0,sizeof(d));
 for (i=1;i<=n;i++)
  for (j=1;j<=m;j++)
   if (a[i][j]=='X')u[i][j]=0;
    else u[i][j]=u[i-1][j]+1;
 for (i=n;i>=1;i--)
  for (j=1;j<=m;j++)
   if (a[i][j]=='X')d[i][j]=0;
    else d[i][j]=d[i+1][j]+1;

 for (i=1;i<=n;i++)
  dp(i);
 for (i=k;i>=1;i--)
 {
  fin[i]=ans;
  a[x[i]][y[i]]='.';
  update(y[i]);
  dp(x[i]);
 }
 for (i=1;i<=k;i++)printf("%d\n",fin[i]);
 return 0;
}