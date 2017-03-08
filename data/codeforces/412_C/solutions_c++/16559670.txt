#include <bits/stdc++.h>

#define FI(i,a,b) for(int i=(a);i<=(b);i++)
#define FD(i,a,b) for(int i=(a);i>=(b);i--)

using namespace std;

char mo[100005],s[100005];
int n,len;

int main(){
  scanf("%d",&n);
  while(n--){
    scanf("\n%s",s);
    len=strlen(s);
    FI(i,0,len-1){
      if(!mo[i]){
        if(s[i]!='?') mo[i]=s[i];
      }else{
        if(mo[i]>='a' && s[i]!=mo[i] && s[i]!='?') mo[i]='?';
      }
    }
  }
  FI(i,0,len-1) if(!mo[i]) mo[i]='a';
  puts(mo);
  return 0;
}