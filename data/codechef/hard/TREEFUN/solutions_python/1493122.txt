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

const int maxn=55555;
const int maxb=18;

int n;
vi e[maxn];
int par[maxb][maxn];
int d[maxn];
int FU[maxn];
int vis[maxn];
int pos[maxn];
int ord;

int cmp(int a, int b){return pos[a]<pos[b];}

int lca2(int a, int b){
    if (d[a]<d[b]) swap(a,b);
    for (int i=maxb-1; i>=0; --i) if (d[par[i][a]]>d[b]) a=par[i][a];
    if (par[0][a]==b) return a;
    return -1;
}

int lca(int a, int b){
    if (d[a]<d[b]) swap(a,b);
    for (int i=maxb-1; i>=0; --i) if (d[par[i][a]]>=d[b]) a=par[i][a];
    for (int i=maxb-1; i>=0; --i) if (par[i][a]!=par[i][b]) a=par[i][a], b=par[i][b];
    return a==b?a:par[0][a];
}



void dfs(int a, int p){
    par[0][a]=p==-1?a:p;
    d[a]=p==-1?0:d[p]+1;
    REP(i,e[a].size()){
        int b=e[a][i];
        if (b!=p) dfs(b,a);
    }
    pos[a]=ord++;
}



int main(){
    int tn; cin>>tn;
    REP(ti,tn){
        int nq;
        cin>>n>>nq;
        REP(i,n-1){
            int a,b; scanf(" %d%d",&a,&b); --a; --b;
            e[a].pb(b); e[b].pb(a);
        }
        ord=0;
        dfs(0,-1);
        FOR(i,1,maxb) REP(j,n) par[i][j]=par[i-1][par[i-1][j]];


        memset(vis,-1,sizeof(vis));
        memset(FU,-1,sizeof(FU));
        REP(step,nq){
            int nx; scanf(" %d",&nx);
            vi tb;
            REP(i,nx){int a; scanf(" %d",&a); tb.pb(a-1); vis[a-1]=step;}
            if (nx==2){
                int c=lca(tb[0],tb[1]);
                printf("%d\n",d[tb[0]]+d[tb[1]]-2*d[c]-1);
            }else{
                int fd=0;
                int aa=0;
                sort(ALL(tb),cmp);

                int u=0;
                REP(i,nx-1){
                    int c=lca(tb[i],tb[i+1]);
                    if (d[c]>d[u]) u=c;
                }
                if (vis[u]!=step){
                    int xx=-1;
                    REP(k,nx){
                        int aa=lca(u,tb[k]);
                        if (aa!=u){
                            if (xx!=-1) goto fail;
                            xx=k;
                        }
                    }
                    REP(k,nx) if (k!=xx){
                        int c=lca2(u,tb[k]);
                        if (c==-1 || FU[c]==step) goto fail;
                        FU[c]=step;
                    }
                    fd=1;
                }
fail:;

                printf("%d\n",fd);

            }
        }
        REP(i,n) e[i].clear();
    }
    return 0;
}

