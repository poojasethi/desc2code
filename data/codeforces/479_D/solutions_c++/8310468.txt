#include<cstdio>
#include<map>
using namespace std;
int n,l,x,y,X,Y,ans,i,a[100005];
map<int,int>M;
void work(int p)
{
  if (p<0||p>l) return;
  if (M[p-y]||M[p+y]) ans=p;
}
int main()
{
  scanf("%d%d%d%d",&n,&l,&x,&y);
  for (i=1;i<=n;i++) scanf("%d",&a[i]),M[a[i]]=1;
  for (i=1;i<=n;i++) 
  {
    X|=(M[a[i]+x]||M[a[i]-x]);
    Y|=(M[a[i]+y]||M[a[i]-y]);
  }
  if (X&&Y) {puts("0");return 0;}
  if (X||Y) 
  {
    puts("1");printf("%d",X?y:x);
    return 0;
  }
  ans=-1;
  for (i=1;i<=n;i++)
  {
    work(a[i]+x);
    work(a[i]-x);
  }
  if (ans==-1) printf("2\n%d %d",x,y);
  else printf("1\n%d",ans);
  return 0;
}
