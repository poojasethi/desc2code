#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int> pii;
typedef long long lli;
const int nmax=1e5+9;
pii e[2*nmax];
lli n,m,q,ans[nmax];
lli a[nmax],b[nmax],c[nmax],d[nmax],k[nmax];
int main(){
   ios_base::sync_with_stdio(false);
   cin.tie(0);
   cin>>n;
   for(int i=1;i<=n;i++){
      cin>>a[i]>>b[i];
   }
   cin>>m;
   for(int i=1;i<=m;i++){
      cin>>c[i]>>d[i]>>k[i];
   }
   for(int i=1;i<=n;i++){
      e[++q]=pii(-b[i],i);
   }
   for(int i=1;i<=m;i++){
      e[++q]=pii(-d[i],-i);
   }
   sort(e+1,e+q+1);
   set<pii> st;
   for(int i=1;i<=q;i++){
      int x=e[i].first,y=e[i].second;
      if(y<0){
         st.insert(pii(-c[-y],-y));
      }
      else{
         set<pii>::iterator it=st.lower_bound(pii(-a[y],0));
         if(it==st.end()){
            cout<<"NO\n";
            return 0;
         }
         ans[y]=it->second;
         if(--k[it->second]==0)st.erase(it);
      }
   }
   cout<<"YES\n";
   for(int i=1;i<=n;i++){
      cout<<ans[i]<<" ";
   }
   cout<<"\n";
}
