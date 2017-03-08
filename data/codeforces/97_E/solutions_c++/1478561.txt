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
const int maxb=20;
int n, m;
vi e[maxn];
int par[maxn][maxb], d[maxn];
int id[maxn];
int idx;


int cycle[2*maxn], odd[2*maxn], nc;
int par2[2*maxn];
int scc[maxn];
int vis[maxn];

int dp[maxn];

int root(int a, int *p){return p[a]==-1?a:p[a]=root(p[a],p);}
void join(int a, int b){
    if (a==b) return;
    if (id[cycle[a]]>id[cycle[b]]) swap(a,b);
    odd[a]|=odd[b];
    par2[b]=a;
}

pii dfs(int a, int p=-1){
    par[a][0]=p==-1?a:p;
    d[a]=p==-1?0:d[p]+1;
    if (p!=-1) scc[a]=root(p,scc);

    int backe=id[a]=idx++;

    //printf("ON %d\n",a);
    int cid=a;
    REP(i,e[a].size()){
        int b=e[a][i];
        if (b==p) continue;
        if (id[b]!=-1){
            if (id[b]<id[a]){
                if (cid==a) cycle[cid=nc++]=b;
                if ((d[a]-d[b])%2==0) odd[cid]|=1;
                if (id[b]<id[cycle[cid]]) cycle[cid]=b;
                checkmin(backe,id[b]);
            }
        }else{
            pii res=dfs(b,a);
            if (res.ST<id[a]){
                if (cid==a) cid=res.ND;
                join(root(cid,par2),root(res.ND,par2));
                checkmin(backe,res.ST);
            }
        }
    }
    if (cid!=a) par2[a]=cid=root(cid,par2);
    //printf("%d >>  %d %d\n", a, backe, id[a]);
    return MP(backe,cid);
}

void dfsb(int a, int p=-1){
    if (vis[a]) return;
    vis[a]=1;
    dp[a]=(p==-1?0:dp[p])
        +(cycle[root(a,par2)]==p?odd[root(a,par2)]:0)
        +(p!=-1&&cycle[root(a,par2)]==cycle[root(p,par2)]?odd[root(a,par2)]:0);
    REP(i,e[a].size()) dfsb(e[a][i],a);
}

int lca(int a, int b){
    if (d[a]>d[b]) swap(a,b);
    for (int i=maxb-1; i>=0; --i) if (d[par[b][i]]>=d[a]) b=par[b][i];
    for (int i=maxb-1; i>=0; --i) if (par[a][i]!=par[b][i]) a=par[a][i], b=par[b][i];
    if (a!=b) a=par[a][0], assert(par[b][0]==a);
    return a;
}

int go(int a, int b){
    if (a==b) return 0;

    if (root(a,scc)!=root(b,scc)) return 0;
    if (d[b]<d[a]) swap(a,b);
    int sa=root(a,par2), sb=root(b,par2);

    //out(dp,n);
    int c=lca(a,b);
    if (d[a]+d[b]-2*d[c]&1) return 1;
    return dp[a]+dp[b]-2*dp[c]>=1;
}

int main(){
    cin>>n>>m;
    REP(i,m){int a, b; scanf(" %d%d", &a,&b); --a; --b; e[a].pb(b); e[b].pb(a);}

    memset(id,-1,sizeof(id));
    memset(par2,-1,sizeof(par2));
    memset(scc,-1,sizeof(scc));
    memset(cycle,-1,sizeof(cycle));
    nc=n;
    REP(i,n) if (scc[i]==-1) dfs(i), dfsb(i);
    //REP(i,n) printf("%d >> %d >> %d xx %d\n", i, root(i,par2), cycle[root(i,par2)], odd[root(i,par2)]);
    //out(dp,n);
    //printf("%d\n", go(4,7));
    //return 0;

    FOR(i,1,maxb) REP(a,n) par[a][i]=par[par[a][i-1]][i-1];

    int nq; cin>>nq;
    REP(step,nq){
        int a, b; scanf(" %d%d", &a,&b); --a; --b;
        //if (nq==190){
        //    if (step>=77) printf("%d %d\n", a, b);
        //    else continue;
        //}
        int res=go(a,b);
        puts(res?"Yes":"No");

    }

    return 0;
}

