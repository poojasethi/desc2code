#include<bits/stdc++.h>
using namespace std;
const int nmax=1e5+9;
int b[nmax],par[nmax];
vector<int> d,p;
int n,m;
int get(int x){
   if(par[x]==0)
      return x;
   else{
      par[x]=get(par[x]);
      return par[x];
   }
}
int main(){
   ios_base::sync_with_stdio(false);
   cin.tie(0);
   cin>>n>>m;
   for(int i=1;i<=m;i++){
      int t;
      cin>>t;
      if(t==1){
         int x,y;
         cin>>x>>y;
         b[x]=y;
         par[x]=y;
      }
      else if(t==2){
         int x;
         cin>>x;
         d.push_back(x);
         p.push_back(get(x));
      }
      else{
         int x,j;
         cin>>x>>j;
         int y=d[j-1],z=p[j-1];
         while(y!=z){
            //cout<<"y="<<y<<"\n";
            if(y==x){
               break;
            }
            y=b[y];
         }
         if(y==x)cout<<"YES\n";
         else cout<<"NO\n";
      }
   }
}
