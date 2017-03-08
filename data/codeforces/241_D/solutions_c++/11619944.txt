#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
int n,p,x,tot,ans;
int num[50],d[50],pos[50];
bool g[32][32][50005];
bool f[32][32][50005];
int add(int x,int y)
{
  x*=10;
  if (y>9) x*=10;
  return (x+y)%p;
}

int Find(int num,int k,int j,int i){
  for (int t=0;t<p;t++)
    if (f[i][j][t] && add(t,num)==k) return t;
  return 0;
}

int main(){
  scanf("%d%d",&n,&p);
  bool flag = 0;
  f[0][0][0] = 1;
  for (int i=1;i<=n;i++){
    scanf("%d",&x);
    if (x<32)
    {
      pos[++tot] = i;
      num[tot] = x;
      for (int j=0;j<32;j++){
        for (int k=0;k<p;k++)
        if (f[tot-1][j][k]){
          f[tot][j][k] = 1;
          int t = add(k,x);
          f[tot][j^x][t] = 1;
          g[tot][j^x][t] = 1;
          if (j==x && t==0)
            {flag=1; break;}
        }
        if (flag) break;
      }
    }
    if (flag) break;
  }

  if (!flag) {puts("No");return 0;}
  puts("Yes");
  int j = 0, k = 0;
  for (int i=tot;i>0;i--)
  if (g[i][j][k]){
    d[++ans] = pos[i];
    j ^= num[i];
    k = Find(num[i], k, j, i-1);
  }
  printf("%d\n",ans);
  while (ans--){
    printf("%d",d[ans+1]);
    if (ans) printf(" ");
      else printf("\n");
  }
  return 0;
}