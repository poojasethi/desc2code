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

template<class T> void checkmin(T &a, T b){if (b<a)a=b;}
template<class T> void checkmax(T &a, T b){if (b>a)a=b;}
template<class T> void out(T t[], int n){REP(i, n)cout<<t[i]<<" "; cout<<endl;}
template<class T> void out(vector<T> t, int n=-1){for (int i=0; i<(n==-1?t.size():n); ++i) cout<<t[i]<<" "; cout<<endl;}
inline int count_bit(int n){return (n==0)?0:1+count_bit(n&(n-1));}
inline int low_bit(int n){return (n^n-1)&n;}
inline int ctz(int n){return (n==0?-1:ctz(n>>1)+1);}
int toInt(string s){int a; istringstream(s)>>a; return a;}
string toStr(int a){ostringstream os; os<<a; return os.str();}

const int mod=1e9+7;
const int maxn=111111;

int n;
int A[maxn];
int sa[maxn], pa[maxn];
int fact[maxn], ifact[maxn];
int sb[maxn], pb[maxn], nodd[maxn];

int faste(int a, int p){int x=1; for (; p; p>>=1, a=1ll*a*a%mod) if (p&1) x=1ll*x*a%mod; return x;}

int main(){
    fact[0]=ifact[0]=1;
    FOR(i,1,maxn) fact[i]=1ll*i*fact[i-1]%mod, ifact[i]=faste(fact[i],mod-2);

    REP(i,maxn) pa[i]=pb[i]=1;


    cin>>n;
    REP(i,n) scanf(" %d", A+i);


    pa[maxn-1]=1;
    sb[maxn-1]=0; pb[maxn-1]=1;
    REP(i,n){
        ++sa[maxn-1]; ++nodd[maxn-1];

        int lb=min(A[i],(int)sqrt(A[i])+1);
        vector<pii> lst;
        FOR(j,1,lb+1) lst.pb(MP(j,(A[i]+j-1)/j));
        assert(lst.size());
        for (int j=lst.back().ND; j>1; --j) lst.pb(MP((int)floor(1.*A[i]/(j-1)-1e-9),j));
        reverse(ALL(lst));

        int last=1;
        REP(j,lst.size()){
            int x=lst[j].ST, v=lst[j].ND;
            sa[x]+=v-last;
            pa[x]=1ll*pa[x]*fact[v]%mod*ifact[last]%mod;

            sb[x]+=v/2-last/2;
            pb[x]=1ll*pb[x]*fact[v/2]%mod*ifact[last/2]%mod;
            nodd[x]+=(v&1)-(last&1);
            last=v;
        }
    }


    for (int i=maxn-2; i>=0; --i) sa[i]+=sa[i+1], sb[i]+=sb[i+1], pa[i]=1ll*pa[i]*pa[i+1]%mod, pb[i]=1ll*pb[i]*pb[i+1]%mod, nodd[i]+=nodd[i+1];

    int nq; cin>>nq;
    REP(i,nq){
        int x; scanf(" %d", &x); x=min(x,maxn-1);
        int u=1ll*fact[sa[x]]*faste(pa[x],mod-2)%mod, v=(nodd[x]<=1?1ll*fact[sb[x]]*faste(pb[x],mod-2)%mod:0);
        int res=1ll*(u-v)*((mod+1)/2)%mod+v;
        res%=mod;
        if (res<0) res+=mod;
        printf("%d\n", res);
    }
    return 0;
}


