#include<bits/stdc++.h>
using namespace std;
#define pb push_back
int k,i,j,br=2,n,m;
vector<int> v;
void solve(int st){
   v.clear();
   for(int i=1;i<k;i++){
      br++;
      cout<<st<<" "<<br<<"\n";
      v.pb(br);
   }
   for(int i=1;i<=(k-1)/2;i++){
      br+=2;
      cout<<br<<" "<<br-1<<"\n";
      for(int j=0;j<k-1;j++){
         cout<<br-1<<" "<<v[j]<<"\n";
         cout<<br<<" "<<v[j]<<"\n";
      }
   }
}
int main(){
   ios_base::sync_with_stdio(false);
   cin>>k;
   if(k%2==0){
      cout<<"NO\n";
      exit(0);
   }
   cout<<"YES\n";
   n=2+4*(k-1);
   m=n*k/2;
   cout<<n<<" "<<m<<"\n";
   cout<<"1 2\n";
   solve(1);
   solve(2);
}
