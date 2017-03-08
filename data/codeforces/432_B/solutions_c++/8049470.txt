#include<cstdio>

const int N=100050;
int n;
int x[N],y[N],f[N];

int main(){
  scanf("%d",&n);
  for(int i=1;i<=n;i++) scanf("%d%d",&x[i],&y[i]),f[x[i]]++;
  for(int i=1;i<=n;i++)
    printf("%d %d\n",n-1+f[y[i]],n-1-f[y[i]]);
}