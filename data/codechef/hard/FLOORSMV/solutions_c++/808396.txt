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

const int maxn=444;
const int inf=1e9;

int n, f;
int g[maxn][maxn];
map<pii,int> mp;
int fa[maxn], px[maxn];
int pos;

vi fl[maxn];

int getid(int a, int b){
    if (mp.count(MP(a,b))) return mp[MP(a,b)];
    px[pos]=a; fa[pos]=b;
    return mp[MP(a,b)]=pos++;
}

ll go(vector<pii> &l){
    ll res=0;
    ll u=f-l.back().ST-1;
    res+=u*(u+1)/2+l.back().ND*u;
    assert(!res);

    REP(i, l.size()) res+=l[i].ND;
    REP(i, l.size()-1){
        int T=l[i].ST, H=l[i+1].ST;
        int a=l[i].ND, b=l[i+1].ND;
        while(T+1<H){
            int M=(T+H)/2;
            if (a+M-l[i].ST>b+l[i+1].ST-M) H=M;
            else T=M;
        }
        int d=T-l[i].ST;
        res+=1ll*d*(d+1)/2+1ll*a*d;
        d=l[i+1].ST-T-1;
        res+=1ll*d*(d+1)/2+1ll*b*d;
    }
    return res;

}

int main(){
    int m; cin>>n>>f>>m;


    REP(i, maxn) REP(j, maxn) g[i][j]=inf;

    pos=0;
    REP(i, m){
        int a, b, c, d, e;
        cin>>a>>b>>c>>d>>e;
        --a,--b,--d,--e;
        int u, v; u=getid(a,b); v=getid(d,e);
        g[u][v]=g[v][u]=c;
    }
    REP(i, n) getid(i, 0);
    REP(i, n) getid(i, f-1);

    REP(i, pos) g[i][i]=0;
    REP(i, pos) REP(j, i){
        int v;
        if (px[i]!=px[j]) v=fa[i]+fa[j]+abs(px[i]-px[j]);
        else v=abs(fa[i]-fa[j]);
        checkmin(g[j][i], v);
        checkmin(g[i][j], v);
    }
    REP(k, pos) REP(i, pos) REP(j, pos) checkmin(g[i][j], g[i][k]+g[k][j]);



    FE(it, mp) fl[it->ST.ST].pb(it->ST.ND);
    REP(i, n) sort(ALL(fl[i]));
    int nq; cin>>nq;
    REP(tq, nq){
        int a, b; cin>>a>>b;
        --a; --b;
        vi::iterator it=lower_bound(ALL(fl[a]), b); 
        int da, db, sta, stb;
        if (it==fl[a].end()) da=db=b-*--it, sta=stb=*it;
        else if (b==*it) da=db=0, sta=stb=b;
        else{ sta=*it, stb=*--it; da=sta-b; db=b-stb; }

        ll res=0;
        vector<pii> tb;
        sta=mp[MP(a,sta)];
        stb=mp[MP(a,stb)];


        //tb.pb(MP(b,0));
        //sort(ALL(tb));
        //REP(i, fl[a].size()) tb.pb(MP(fl[a][i], min(da+g[sta][mp[MP(a,fl[a][i])]], db+g[stb][mp[MP(a,fl[a][i])]])));
        //res+=go(tb);

        REP(j, n) if (j!=a){
            tb.clear();
            REP(i, fl[j].size()) tb.pb(MP(fl[j][i], min(da+g[sta][mp[MP(j,fl[j][i])]], db+g[stb][mp[MP(j,fl[j][i])]])));
            res+=go(tb);
        }
        cout<<res<<endl;
    }
    return 0;
}



