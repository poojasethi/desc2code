#include <cstdio>
using namespace std;

int x[105][105],time[105],n,m,k,cnt[105];
bool locked[105];

int main(){
 scanf("%d %d %d",&n,&m,&k);
 for(int i=1;i<=n;i++)
  for(int j=1;j<=m;j++)
   scanf("%d",&x[i][j]);
 for(int i=1;i<=m;i++){
  for(int j=1;j<=k;j++)
   cnt[j]=0;
  for(int j=1;j<=n;j++)
   if(time[j]==0 && x[j][i]>0 && !locked[x[j][i]])
    cnt[x[j][i]]++;
  for(int j=1;j<=k;j++)
   if(cnt[j]>1) locked[j]=1;
  for(int j=1;j<=n;j++)
   if(time[j]==0 && x[j][i]>0 && locked[x[j][i]])
    time[j]=i;
 }
 for(int i=1;i<=n;i++)
  printf("%d\n",time[i]);
 return 0;
}