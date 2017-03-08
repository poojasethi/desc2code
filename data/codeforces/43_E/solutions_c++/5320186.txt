#include <cstdio>

using namespace std;
int ans,n,s,i,j,S[1001],v[101][1001],T[101][1001];
int x1,x2,x3,x4,t,tt,p1,p2;

bool pd(){
  if (x3!=x4) return ((x1-x2)<0 && (x3-x4)>0) || ((x1-x2)>0 && (x3-x4)<0);
  if (x3==s) return 0;
  int q1=p1,q2=p2;
  if (tt==T[i][q1]) q1++;
  if (tt==T[j][q2]) q2++;
  if ( (x1<x2 && v[i][q1]>v[j][q2]) || (x1>x2 && v[i][q1]<v[j][q2]) ) return 1;
  return 0;
}

int main(){
  //freopen("43E.in","r",stdin);
  //freopen("43E.out","w",stdout);
  scanf("%d%d",&n,&s);
  for (i=1;i<=n;i++){
    scanf("%d",&S[i]);
    for (j=1;j<=S[i];j++){
      scanf("%d%d",&v[i][j],&T[i][j]);
      T[i][j]+=T[i][j-1];
    }
  }
  for (i=1;i<=n;i++)
    for (j=i+1;j<=n;j++){
      x1=x2=0;
      t=0;
      p1=p2=0;
      while (x1<s && x2<s){
        if (p1<S[i] && t==T[i][p1]) p1++;
        if (p2<S[j] && t==T[j][p2]) p2++;
        if (T[i][p1]<T[j][p2]) tt=T[i][p1];
          else tt=T[j][p2];
        x3=x1+(tt-t)*v[i][p1];
        x4=x2+(tt-t)*v[j][p2];
        if ( pd() )  ans++;
        x1=x3;x2=x4;
        t=tt;
      }
    }
  printf("%d\n",ans);
  return 0;
}