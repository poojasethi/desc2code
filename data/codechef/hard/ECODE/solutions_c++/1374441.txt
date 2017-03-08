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

const int maxn=13;
int n;
ll a,mod,g;
ll pw[maxn];
ll pw10[maxn];

ll mul(ll x, ll y){
    ll res=0;
    while(y){
        res+=x*(y&1023);
        y>>=10;
        x=(x<<10)%mod;
        res%=mod;
    }
    return res;
}


int main(){
    cin>>n>>a>>mod>>g;
    pw[0]=1;
    pw10[0]=1;
    REP(i,n) pw[i+1]=mul(a,pw[i]);
    REP(i,n) pw10[i+1]=10*pw10[i];

    int na=pw10[n/2], nb=pw10[(n+1)/2];
    vector<pair<ll,int> > tb;
    REP(i,nb){
        int u=i;
        ll x=0;
        REP(j,(n+1)/2){ x=(x+u%10*pw[j])%mod; u/=10; }
        tb.pb(MP(x,i));
    }
    sort(ALL(tb));


    ll res=-1;
    REP(i,na){
        int u=i;
        ll x=0;
        REP(j,n/2){ x=(x+u%10*pw[(n+1)/2+j])%mod; u/=10; }
        x=(g+mod-x)%mod;
        vector<pair<ll,int> >::iterator it=lower_bound(ALL(tb),MP(x,0));
        if (it!=tb.end() && it->ST==x){res=1ll*i*pw10[(n+1)/2]+it->ND; break;}
    }
    vi s(n,0);
    REP(i,n) s[n-1-i]=res%10, res/=10;
    REP(i,n) printf("%d",s[i]); puts("");
    return 0;
}

