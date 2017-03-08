#include <bits/stdc++.h>
using namespace std;
main(){
	
  int a,b,c,x,y,z;
  cin>>a>>b>>c>>x>>y>>z;
  int r,t,u;
  r=a-x;
  t=b-y;
  u=c-z;
  if(r>=0)
    r/=2;
  if(t>=0)
    t/=2;
  if(u>=0)
    u/=2;
  if(r+t+u>=0)
    cout<<"Yes"<<endl;
  else
    cout<<"No"<<endl;
}
