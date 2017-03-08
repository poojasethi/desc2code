#include<bits/stdc++.h>

#define FI(i,a,b) for(int i=(a);i<=(b);i++)
#define FD(i,a,b) for(int i=(a);i>=(b);i--)

#define LL long long

using namespace std;

int n,res=6;
char s[1005][8];

int main(){
  scanf("%d",&n);
  FI(i,1,n) scanf(" %s",s[i]+1);
  FI(i,1,n) FI(j,i+1,n){
    int cnt=0;
    FI(k,1,6) cnt+=s[i][k]!=s[j][k];
    res=min(res,(cnt-1)/2);
  }
  printf("%d\n",res);
  return 0;
}