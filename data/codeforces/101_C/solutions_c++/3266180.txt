#include<iostream>
#include<cstdio>
#include<queue>
#include<map>
#define test puts("OK");
#define LL long long
#define mp(a,b) make_pair(a,b)
using namespace std;
LL ax,ay,bx,by,cx,cy;
LL t;
bool check(LL x,LL y){
  if(!t){
    if(x==bx&&y==by) return true;
    else return false;
  }
  if((cx*bx+cy*by-x*cx-y*cy)%(t)==0&&(bx*cy-by*cx-x*cy+y*cx)%(t)==0)
    return true;
  return false;
}
int main(){
  cin>>ax>>ay>>bx>>by>>cx>>cy;
  t=cx*cx+cy*cy;
  if(check(ax,ay)) puts("YES");
  else if(check(ay,-ax)) puts("YES");
  else if(check(-ax,-ay)) puts("YES");
  else if(check(-ay,ax)) puts("YES");
  else puts("NO");
  return 0;
}