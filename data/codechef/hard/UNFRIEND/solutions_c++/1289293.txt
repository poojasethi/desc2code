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

const int maxn=55;
const int maxm=2*222;
int n,m,w,N,nm;
int to[maxm], from[maxm];
int vis[maxn], par[maxn];

int lst[maxm], is[maxm];
ll val[maxn][4];
ll el[4];


ll M[maxm][4];

void dfs(int a, int p=-1){
    if (vis[a]) return;
    vis[a]=1;
    memcpy(val[a],el,sizeof(el));
    par[a]=p;
    REP(i,2*m) if (from[i]==a && to[i]!=p){
        int u=i/2;
        el[u/64]|=1ll<<(u%64);
        dfs(to[i],a);
        el[u/64]^=1ll<<(u%64);
    }
}

int solve(){
    int u=0;
    REP(i,w){
        int p=-1;
        int x=lst[i]/64, y=lst[i]%64;
        FOR(j,u,nm) if (M[j][x]&(1ll<<y)){p=j; break;}
        if (p==-1) continue;
        REP(k,4) swap(M[p][k],M[u][k]);
        REP(j,nm) if (j!=u && (M[j][x]&(1ll<<y))) REP(k,4) M[j][k]^=M[u][k];
        ++u;
    }

    REP(i,nm){
        int fd=0;
        REP(j,w) if (M[i][lst[j]/64]&(1ll<<lst[j]%64)){fd=1; break;}
        if (fd) continue;
        FOR(j,w,m) if (M[i][lst[j]/64]&(1ll<<lst[j]%64)) fd^=1;
        if (fd) return 0;
    }
    return 1;
}

int main(){
    int tn; cin>>tn;
    REP(ti,tn){
        cin>>n>>m;
        memset(is,0,sizeof(is));
        REP(i,m){int a,b; scanf(" %d%d",&a,&b); --a; --b; from[2*i]=b; to[2*i]=a; from[2*i+1]=a; to[2*i+1]=b;}
        cin>>w;
        REP(i,w){int a; scanf(" %d",&a); --a; is[a]=1; lst[i]=a;}
        int pos=w;
        REP(i,m) if (!is[i]) lst[pos++]=i;

        memset(vis,0,sizeof(vis)); memset(el,0,sizeof(el));
        N=(m+63)/64;
        REP(i,n) if (!vis[i]) dfs(i);

        nm=0;
        REP(i,m){
            int a=to[2*i], b=from[2*i];
            if (par[a]!=b && par[b]!=a){
                REP(j,4) M[nm][j]=val[a][j]^val[b][j];
                M[nm][i/64]|=1ll<<i%64;
                ++nm;
            }
        }
        puts(solve()?"YES":"NO");

    }
    return 0;
}

