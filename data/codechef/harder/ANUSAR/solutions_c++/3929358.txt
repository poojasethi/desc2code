#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <string>
#include <cmath>
#include <ctime>
#include <utility>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <sstream>
#define FOR(a,b,c) for (int a=b,_c=c;a<=_c;a++)
#define FORD(a,b,c) for (int a=b;a>=c;a--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; ++i)
#define REPD(i,a) for(int i=(a)-1; i>=0; --i)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define sz(a) int(a.size())
#define reset(a,b) memset(a,b,sizeof(a))
#define oo 1000000007

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

const int maxn=200007;

int SA[maxn],tSA[maxn],RA[maxn],tRA[maxn],cnt[maxn],PLCP[maxn],LCP[maxn],prev[maxn];
int n,mys[maxn],last,m,L[maxn],R[maxn];
ll f[maxn];
vector<int> pos[maxn];
char s[maxn];

int fRA(int i){
    if(i<=n) return RA[i]; else return 0;    
}

void sort(int k){
    int maxv=max(300,n);
    FOR(i,0,maxv) cnt[i]=0;
    FOR(i,1,n) ++cnt[fRA(SA[i]+k)];
    for(int i=0, t,sum=0; i<=maxv; ++i){
        t=sum;
        sum+=cnt[i];
        cnt[i]=t;   
    }
    FOR(i,1,n) tSA[++cnt[fRA(SA[i]+k)]]=SA[i];
    FOR(i,1,n) SA[i]=tSA[i];
}

void construct(){
    int r;
    
    FOR(i,1,n) SA[i]=i, RA[i]=s[i]; 
    for(int k=1; k<n; k*=2){
        sort(k); sort(0);
        tRA[SA[1]]=r=1;   
        FOR(i,2,n){
            if(RA[SA[i]]!=RA[SA[i-1]] || fRA(SA[i]+k)!=fRA(SA[i-1]+k)) ++r;
            tRA[SA[i]]=r;   
        }
        FOR(i,1,n) RA[i]=tRA[i];
    }  
    
    prev[SA[1]]=-1;
    FOR(i,2,n) prev[SA[i]]=SA[i-1];
    int l=0;
    FOR(i,1,n){
        if(prev[i]==-1){
            PLCP[i]=0;
            continue;   
        }   
        while(i+l<=n && prev[i]+l<=n && s[i+l]==s[prev[i]+l]) ++l;
        PLCP[i]=l;
        l=max(l-1,0);
    }
    LCP[0]=LCP[n+1]=0;
    FOR(i,1,n) LCP[i]=PLCP[SA[i]];
}

int main(){
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    REP(tt,t){
        scanf("%s",s+1);
        n=strlen(s+1);  
        construct();
        
        last=0;
        FOR(i,1,n){
            while(last>0 && LCP[mys[last]]>=LCP[i]) --last;
            if(last>0) L[i]=mys[last]+1; else L[i]=1;
            mys[++last]=i;   
        }
        last=0;
        FORD(i,n,1){
            while(last>0 && LCP[mys[last]]>=LCP[i]) --last;
            if(last>0) R[i]=mys[last]-1; else R[i]=n;   
            mys[++last]=i;
        }
        FOR(i,1,n) f[i]=0;
        FOR(i,1,n) pos[i].clear();
        FOR(i,1,n) if(LCP[i]>0) pos[LCP[i]].pb(i);  
         
        FOR(i,1,n){
            int right=0;
            REP(j,sz(pos[i])){
                int p=pos[i][j];
                if(p<=right) continue;
                f[R[p]-L[p]+2]+=1ll* min(LCP[p],min(LCP[p]-LCP[R[p]+1],LCP[p]-LCP[L[p]-1])) * (R[p]-L[p]+2);
                right=R[p];
            }   
        }
        
        FORD(i,n-1,2) f[i]+=f[i+1];
        f[1]=1ll*n*(n+1)/2;
        
        int q,v;
        scanf("%d",&q);
        REP(i,q){
            scanf("%d",&v);            
            printf("%lld\n", v>n?0ll:f[v]);   
        }
    }
    
    return 0;
}
