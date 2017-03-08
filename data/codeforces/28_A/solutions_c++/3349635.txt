#include <cstdio>
#include <iostream>
#include <cmath>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <complex>
#include <algorithm>
#include <functional>
#include <fstream>
#include <numeric>
#include <string>
#include <valarray>


using namespace std;

const int MAX_N=500+20;

int n,m,x[MAX_N],y[MAX_N];

int main(){
  cin>>n>>m;
  for (int i=1;i<=n;i++)
    cin>>x[i]>>y[i];
  x[0]=x[n];
  y[0]=y[n];
  x[n+1]=x[1];
  y[n+1]=y[1];
  x[n+2]=x[2];
  y[n+2]=y[2];
  map<int,vector<int> > Map;
  for (int i=1;i<=m;i++){
    int temp;
    cin>>temp;
    Map[temp].push_back(i);
  }
  map<int,vector<int> > p=Map;
  for (int start=1;start<=2;start++){
    Map=p;
    vector<int> ans(n+1,-1);
    bool bad=false;
    for (int j=start;j<=n;j+=2){
      int t=abs(x[j]-x[j-1])+
    abs(y[j]-y[j-1])+
    abs(x[j]-x[j+1])+
    abs(y[j]-y[j+1]);
      if (Map[t].size() == 0)
    bad=true;
      else{
    ans[j]=Map[t].back();
    Map[t].pop_back();
      }
    }
    if (!bad){
      cout<<"YES"<<endl;
      for (int i=1;i<ans.size();i++)
    cout<<ans[i]<<' ';
      cout<<endl;
      return(0);
    }
  }
  cout<<"NO"<<endl;
}