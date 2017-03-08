#include <iostream>
#include <cmath>
#include <fstream>

#define rep(i,n) for(int i=0;i<n;i++)

using namespace std;

int n,c,r;

int main(){

  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);

  cin>>n;
  while(1<<r<n)r++;cout<<r<<endl;

  rep(i,r){
    c = 0;
    rep(j,n)if(j>>i&1)c++;cout<<c<<" ";
    rep(j,n)if(j>>i&1)cout<<j+1<<" ";cout<<endl;
  }

}