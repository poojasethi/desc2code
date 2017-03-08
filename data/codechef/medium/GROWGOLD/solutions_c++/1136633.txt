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

const int mod=1e8+7;
int N;
struct matrix{
    matrix(){memset(m,0,sizeof(m));}
    void ident(){memset(m,0,sizeof(m)); REP(i,N) m[i][i]=1;}
    matrix(matrix &a){memcpy(m,a.m,sizeof(m));}
    matrix operator*(const matrix &a)const{ matrix b; REP(i,N) REP(j,N){ ll v=0; REP(k,N) v+=1ll*m[i][k]*a.m[k][j]; b.m[i][j]=v%(mod-1); } return b; }
    int m[111][111];
};
matrix faste(matrix a, int p){ matrix x; x.ident(); for (; p; p>>=1, a=a*a) if (p&1) x=x*a; return x; }
ll faste(ll a, int p){ ll x=1; for (; p; p>>=1, a=a*a%mod) if (p&1) x=x*a%mod; return x; }

int xo, na, nb, K, Nx;

int go(){
    int x=xo;
    --Nx;
    vi l; l.pb(x);

    REP(i,na) if (Nx) --Nx, l.pb(++x);
    REP(i,nb) if (Nx) --Nx, l.pb(x=x*2%mod);

    if (!Nx) return x;

    matrix a;
    N=K+1;
    REP(i,K) a.m[0][i]=1, a.m[i+1][i]=1;
    a=faste(a,Nx);
    int res=1;
    REP(i,K) res=1ll*res*faste(l[l.size()-1-i],a.m[0][i])%mod;
    return res;

}
int main(){
    int tn; cin>>tn;
    REP(ti,tn){
        cin>>xo>>na>>nb>>K>>Nx;
        cout<<go()<<endl;
    }
    return 0;
}


