#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <climits>
//#include <ext/hash_map>


using namespace std;
using namespace __gnu_cxx;



#define REP(i,n) for(int i = 0; i < int(n); ++i)
#define REPV(i, n) for (int i = (n) - 1; (int)i >= 0; --i)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); ++i)

#define FE(i,t) for (__typeof((t).begin())i=(t).begin();i!=(t).end();++i)
#define FEV(i,t) for (__typeof((t).rbegin())i=(t).rbegin();i!=(t).rend();++i)

#define two(x) (1LL << (x))
#define ALL(a) (a).begin(), (a).end()


#define pb push_back
#define ST first
#define ND second
#define MP(x,y) make_pair(x, y)

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef unsigned int uint;



template<class T> void checkmin(T &a, T b){if (b<a)a=b;}
template<class T> void checkmax(T &a, T b){if (b>a)a=b;}
template<class T> void out(T t[], int n){REP(i, n)cout<<t[i]<<" "; cout<<endl;}
template<class T> void out(vector<T> t, int n=-1){for (int i=0; i<(n==-1?t.size():n); ++i) cout<<t[i]<<" "; cout<<endl;}
inline int count_bit(int n){return (n==0)?0:1+count_bit(n&(n-1));}
inline int low_bit(int n){return (n^n-1)&n;}
inline int ctz(int n){return (n==0?-1:ctz(n>>1)+1);}
int toInt(string s){int a; istringstream(s)>>a; return a;}
string toStr(int a){ostringstream os; os<<a; return os.str();}

const int maxn=66;
const int maxb=8888;

int n,b;
char buf[10];
uint x[maxn*maxn+maxb];
ll a[maxn];
ll u[maxb];
int is[maxn];

void go(int x){
    u[x]=0;

    int uu=-1;
    for (int i=0,c=0; i<n; ++c,++i){
        int p=-1;
        FOR(j,i,n) if (a[j]>>c&1){p=j; break;}
        if (p==-1 && uu!=-1) return;
        if (p==-1){uu=c; --i; continue;}

        swap(a[i],a[p]);
        REP(j,n) if (j!=i && (a[j]>>c&1)) a[j]^=a[i];
    }
    if (uu==-1) uu=n;
    u[x]|=1ll<<uu;
    
    REP(i,n) u[x]|=(a[i]>>uu&1ll)<<i;

}

int main(){
    int tn; cin>>tn;
    REP(ti,tn){
        scanf(" %d%d",&n,&b);
        REP(i,b){
            scanf(" %s",buf);
            memset(a,0,sizeof(a));
            if (buf[2]=='w'){
                REP(j,n) REP(k,n){
                    int v; scanf(" %d",&v);
                    a[j]|=(v&1ll)<<k;
                }
            }else{
                uint s,p,b; scanf(" %u%u%u",&s,&p,&b);
                REP(j,n*n) x[j]=s, s=1ll*p*s+b;
                REP(j,n) REP(k,n) a[j]|=((1+(x[j*n+k]>>12))&1ll)<<k;
            }
            REP(j,n) a[j]|=1ll<<n;
            go(i);
        }

        int res=0;
        int nx=n==1?1:0;
        REP(i,b) REP(j,i) res+=nx+__builtin_popcountll(u[i]&u[j])&1;
        printf("%d\n",res);
    }
    return 0;
}

