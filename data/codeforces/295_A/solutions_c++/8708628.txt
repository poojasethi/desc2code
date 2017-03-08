#include<stdio.h>
#define maxn 100100

int p[maxn][3];

int q[maxn],qq[maxn];

long long int ans[maxn];
int i,j,n,m,k;
int main(){
  scanf("%d %d %d",&n,&m,&k);
  for(i=1;i<=n;i++)
    scanf("%d",&q[i]);
  for(i=1;i<=m;i++)
    scanf("%d %d %d",&p[i][0],&p[i][1],&p[i][2]);
  int a,b;
  for(i=1;i<=k;i++){
    scanf("%d %d",&a,&b);
    qq[a]++;
    qq[b+1]--;
  }
  long long int now=0;
  for(i=1;i<=m;i++){
    now+=qq[i];
    ans[p[i][0]]+=now*p[i][2];
    ans[p[i][1]+1]-=now*p[i][2];
  }
  now=0;
  for(i=1;i<=n;i++){
    now+=ans[i];
    printf("%I64d ",now+q[i]);
  }
  return 0;
}
