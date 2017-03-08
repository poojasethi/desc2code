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

const int maxn=77777;
vector<pii> e[maxn];
int n;
int vis[maxn];
ll val[maxn];

int dfs(int a, ll v){
    if (vis[a]) return val[a]!=v;
    vis[a]=1; val[a]=v;
    FE(it,e[a]) if (dfs(it->ST, v-it->ND)) return 1;
    return 0;
}

int doit(){
    memset(vis,0,sizeof(vis));
    val[0]=0;
    if (dfs(0,0)) return 0;
    FOR(i,1,n+1) if (!vis[i]){
        val[i]=val[i-1];
        if (dfs(i, val[i])) return 0;
    }
    return 1;

}

int main(){
    int m;
    cin>>n>>m;
    REP(i,m){
        int a, b, c; cin>>a>>b>>c;
        e[b].pb(MP(a-1,c));
        e[a-1].pb(MP(b,-c));
    }
    if (!doit()) puts("-1");
    else{
        FOR(i,1,n+1) printf("%Ld ", val[i]-val[i-1]);
        puts("");
    }


    return 0;
}


