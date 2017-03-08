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

const int maxn=111111;
const double pi=acos(-1.);
const double eps=1e-9;

int n,m;
int x[maxn], y[maxn];
int vis[maxn];
vector<pii> e[maxn];
vector<double> angl[maxn];
vi F[maxn];

double ang[maxn];
int tb[maxn];

int cmp(const pii &a, const pii &b){ return ang[a.ST]<ang[b.ST]; }
ll dot(int a, int b, int c, int d){return 1ll*a*d-1ll*b*c;}


int dfs(int a, int p=-1){
    if (vis[a]) return 0;
    vis[a]=1;
    
    int ex=-1, cnt=1;
    int m=e[a].size();

    REP(i,m){
        int b=e[a][i].ST;
        if (b==p){ex=i; continue;}
        cnt+=(e[a][i].ND=dfs(b,a));
    }
    if (ex!=-1) e[a][ex].ND=-cnt;

    REP(i,m){
        int b=e[a][i].ST;
        ang[b]=atan2(y[b]-y[a],x[b]-x[a]);
    }
    sort(ALL(e[a]),cmp);

    angl[a].resize(m);
    REP(i,m) angl[a][i]=ang[e[a][i].ST];

    F[a].resize(2*m+1);
    F[a][0]=0;
    REP(i,2*m) F[a][i+1]=F[a][i]+e[a][i%m].ND;
    return cnt;
}


int main(){
    while(scanf(" %d",&n)>0){
        cin>>m;
        REP(i,m){int a, b; scanf(" %d%d",&a,&b); --a; --b; e[a].pb(MP(b,0)); e[b].pb(MP(a,0));}
        REP(i,n) scanf(" %d%d",x+i,y+i);

        int best=0;
        REP(i,n) if (x[i]<x[best]) best=i;

        memset(vis,0,sizeof(vis));
        dfs(best);

        int nq; cin>>nq;
        REP(qq,nq){
            int u; scanf(" %d",&u);
            REP(i,u) scanf(" %d",tb+i), --tb[i];

            int xl=0;
            REP(i,u) if (x[tb[i]]<x[tb[xl]] || (x[tb[i]]==x[tb[xl]] && y[tb[i]]<y[tb[xl]])) xl=i;
            int aa=tb[(xl+1)%u], bb=tb[xl], cc=tb[(xl+u-1)%u];
            if (dot(x[aa]-x[bb],y[aa]-y[bb],x[cc]-x[bb],y[cc]-y[bb])<0) reverse(tb,tb+u);

            tb[u]=tb[0]; tb[u+1]=tb[1];

            int res=u;
            REP(i,u){
                int aa=tb[i+1], bb=tb[i], cc=tb[i+2];
                double ua=atan2(y[bb]-y[aa],x[bb]-x[aa])-eps, ub=atan2(y[cc]-y[aa],x[cc]-x[aa])-eps;
                int pa=lower_bound(ALL(angl[aa]),ub)-angl[aa].begin(), pb=lower_bound(ALL(angl[aa]),ua)-angl[aa].begin();
                if (pb<pa) pb+=angl[aa].size();
                res+=F[aa][pb]-F[aa][pa+1];
            }
            printf("%d\n",res);
        }

        REP(i,n) e[i].clear(), F[i].clear(), angl[i].clear();
    }
    return 0;
}


