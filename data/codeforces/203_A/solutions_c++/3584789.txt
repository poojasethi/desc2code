#include <iostream>
#include<cstring>
using namespace std;
int main(){
	int x,t,a,b,da,db,j,k,s;
        cin>>x>>t>>a>>b>>da>>db;
  for(j=0; j<t; j++)
    for(k=0; k<t; k++)
       if ((a-(j*da)+b-(k*db))==x || a-(j*da)==x || x==0 || b-(k*db)==x) {cout<<"YES"; return 0; }
cout<<"NO";
return 0;
}