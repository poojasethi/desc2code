#include <iostream>
#include <cstdio>
using namespace std;
long long h,w,t,p=1,a,b;
int main(){
  cin>>h>>w;
  for(int i=0;i<=30;i++){
    if(p<=h&&4*p<=5*w){
      t=min(w,5*p/4);
      if(p*t>a*b||(p*t==a*b&&a<p))
        a=p,b=t;
    }
    if (p<=w&&4*p<=5*h){
      t=min(h,5*p/4);
      if (p*t>a*b||(p*t ==a*b&&a<t))
        a=t,b=p;
    }
    p*=2;
  }
  cout<<a<<" "<<b;
  return 0;
}
