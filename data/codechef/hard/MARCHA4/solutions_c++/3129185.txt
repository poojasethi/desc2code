#include<cstdio>
#include<iostream>
#include<vector>
#include<cstring>
#include<algorithm>
#include<numeric>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<list>
#include<climits>
#include<cstdlib>
#include<string>
#include<cmath>

using namespace std;

#define eps 1e-19
#define rev(s,e) reverse(s,e)
#define mset(s,i) memset(s,i,sizeof(s))
#define cpy(i,j) memset(i,j,sizeof(j))
#define mp(x,y) make_pair(x,y)
#define ff first
#define ss second
#define ld long double
#define li long int
#define lli long long int
#define pb(x) push_back(x)
#define f(i,a,b) for(int i=a;i<b;i++)
#define fr(i,a,b) for(int i=a;i>b;i--)

//returning the first k digits
int fst(int n,int k){
  ld t=n*1.0*log10l(n*1.0);
  lli len=(long long)(t)+1;
  lli kk=len-k;
  ld x=pow(10,t-(long double)kk);
 return (int)(x);
}

//returns the power mod k
int mod_pow(int x,int y,int k){
  int tmp=x,ans=1;
  for(;y;y>>=1){
    if(y&1){
      ans=((long long)ans*tmp)%k;
    }
    tmp=((long long)tmp*tmp)%k;
  }
  return ans;
}

int main(){
  int t,n,k;
  cin>>t;
  while(t--){
    cin>>n>>k;
    int k10=pow(10,k);
    cout<<fst(n,k)<<" ";
    int ans=mod_pow(n,n,k10);
    //print requird number of zero so that we print last k digits
    for(k10=k10/10; k10>1 && ans<k10;k10=k10/10){
      cout<<0;
    }
    cout<<ans<<endl;
  }
}
