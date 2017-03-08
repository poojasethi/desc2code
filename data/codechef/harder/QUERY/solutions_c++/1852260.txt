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
#include<sys/resource.h>
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
typedef unsigned int uint;
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

const int maxb=17;
const int maxn=100222;
const int maxs=4*2*maxb*maxn;

vi e[maxn];
int n;
char buf[11];

int par[maxb][maxn];
int d[maxn];
int sz[maxn];
int with[maxn];
void* tmp[maxn];

int N;
int pos,pos2;
int POS;
int rmp[maxn];

struct node2* getn2();

struct node{
    int T,H;
    ll v[2];
    ll val;
    node *l,*r;

    void init(int a, int b);
    node* update(int a, int b, ll v0, ll v1);
    ll getv(ll,ll);
    ll getv(int a, int b,ll,ll);
    void copy(node*);
}tb[maxs];

struct node2{
    int T,H;
    node2 *l,*r;
    void copy(node2 *a){memcpy(a,this,sizeof(node2));}

    void init(int a, int b){
        T=a; H=b;
        if (T+1==H) l=(node2*)tmp[a];
        else{
            l=getn2(); r=getn2();
            l->init(a,a+b>>1);
            r->init(a+b>>1,b);
        }
    }
    node2* update(int a, node* p){
        if (T>a || H<=a) return this;
        node2 *cur=getn2();
        copy(cur);
        if (T+1==H){cur->l=(node2*)p; return cur;}
        cur->l=l->update(a,p);
        cur->r=r->update(a,p);
        return cur;
    }

    node* get(int a){
        if (T+1==H) return (node*)l;
        return a>=T+H>>1?r->get(a):l->get(a);
    }

}tb2[maxn*maxb*maxb*2];


node2 *ver[2*maxn];
node2 *CUR;

node *getn(){assert(pos<maxs);return tb+pos++;}
node2 *getn2(){assert(1||pos2<maxn*maxb*maxb);return tb2+pos2++;}



void node::copy(node *x){ memcpy(x,this,sizeof(node));}
void node::init(int a, int b){
    T=a; H=b;
    if (a+1==b);
    else{
        l=getn(); r=getn();
        l->init(a,a+b>>1);
        r->init(a+b>>1,b);
    }
}

ll node::getv(ll v0, ll v1){int have=H-T; assert(1|| 1.*v1*have*have<5e18);return val+1ll*T*v1*have+1ll*have*v0+1ll*v1*have*(have-1)/2;}
ll node::getv(int a, int b, ll v0, ll v1){
    if (T>=b || H<=a) return 0;
    v0+=v[0]; v1+=v[1];
    if (a<=T && H<=b) return getv(v0,v1);
    return l->getv(a,b,v0,v1)+r->getv(a,b,v0,v1);
}

node* node::update(int a, int b, ll v0, ll v1){
    if (T>=b || H<=a) return this;
    node *nx=getn();
    copy(nx);

    if (a<=T && H<=b){ nx->v[0]+=v0, nx->v[1]+=v1; return nx;}
    nx->l=l->update(a,b,v0,v1);
    nx->r=r->update(a,b,v0,v1);
    nx->val=nx->l->getv(nx->l->v[0],nx->l->v[1])+nx->r->getv(nx->r->v[0],nx->r->v[1]);
    //assert(nx->val>=0);
    return nx;
}


int lca(int a, int b){
    if (d[a]<d[b]) swap(a,b);
    for (int i=maxb-1; i>=0; --i) if (d[par[i][a]]>=d[b]) a=par[i][a];
    for (int i=maxb-1; i>=0; --i) if (par[i][a]!=par[i][b]) a=par[i][a], b=par[i][b];
    if (a!=b) a=par[0][a];
    return a;
}

void dfs(int a, int p=-1){
    par[0][a]=p==-1?a:p;

    d[a]=p==-1?0:d[p]+1;
    sz[a]=1;
    REP(i,e[a].size()){
        int b=e[a][i];
        if (b==p) continue;
        dfs(b,a);
        sz[a]+=sz[b];
    }
}

void dfs_hl(int a, int p=-1, int nh=-1){
    if (nh==-1) nh=a;

    int fd=0;
    REP(i,e[a].size()){
        int b=e[a][i];
        if (b==p) continue;
        if (2*sz[b]>sz[a]-1){ fd=1; dfs_hl(b,a,nh); }
        else dfs_hl(b,a,-1);
    }
    with[a]=nh;

    if (!fd){
        node *x=getn();
        x->init(d[nh],d[a]+1);
        rmp[nh]=POS; tmp[POS++]=x;
    }
}

ll get(int a, int dx){
    ll res=0;
    while(d[a]>=dx){
        int xx=rmp[with[a]];
        node *v=CUR->get(xx);
        res+=v->getv(dx,d[a]+1,0,0);
        
        a=with[a];
        if (par[0][a]==a) break;
        a=par[0][a];
    }
    return res;
}


void go(int a, int dx, ll A, ll B){
    while(d[a]>=dx){
        int xx=rmp[with[a]];
        node *v=CUR->get(xx);
        v=v->update(dx,d[a]+1,A,B);
        CUR=CUR->update(xx,v);

        a=with[a];
        if (par[0][a]==a) break;
        a=par[0][a];
    }
}

void setstack(){

    const rlim_t kStackSize = 256 * 1024L * 1024L;  
    struct rlimit rl;
    int result;

    result = getrlimit(RLIMIT_STACK, &rl);
    if (result == 0)
    {
        if (rl.rlim_cur < kStackSize)
        {
            rl.rlim_cur = kStackSize;
            result = setrlimit(RLIMIT_STACK, &rl);
            if (result != 0)
            {
                fprintf(stderr, "setrlimit returned result = %d\n", result);
                exit(-1);
            }
        }
    }
}


int main(){
    setstack();
    int nq; cin>>n>>nq;

    REP(i,n-1){
        int a, b;
        scanf(" %d%d",&a,&b);
        --a; --b;
        e[a].pb(b);
        e[b].pb(a);
    }

    N=0;
    dfs(0);
    REP(i,maxb-1) REP(j,n) par[i+1][j]=par[i][par[i][j]];
    dfs_hl(0);

    int ns=0;
    ver[ns++]=CUR=getn2();
    CUR->init(0,POS);

    ll ans=0;


    if (0){
        printf(">> %d\n",sizeof(node));
        printf("%d\n",sizeof(tb)/1024/1024);
        printf("%d\n",sizeof(tb2)/1024/1024);
        return 0;
    }

    REP(qq,nq){
        scanf(" %s",buf);
        if (buf[0]=='c'){
            int a,b,A,B; 
            scanf(" %d%d%d%d",&a,&b,&A,&B);

            a=(a+ans)%n;
            b=(b+ans)%n;
            int c=lca(a,b);

            go(a,d[c],A+1ll*B*d[a],-B);
            assert(CUR);
            int dx=d[a]-d[c];
            go(b,d[c]+1,A+1ll*B*(dx-d[c]),B);
            ver[ns++]=CUR;
        }else if (buf[0]=='q'){
            int a,b;
            scanf(" %d%d",&a,&b);
            a=(a+ans)%n;
            b=(b+ans)%n;
            int c=lca(a,b);

            ll res=get(b,d[c])+get(a,d[c]+1);
            printf("%Ld\n",res);
            ans=res;
        }else{
            int uu;
            scanf(" %d",&uu);

            uu=(uu+ans)%ns;
            CUR=ver[uu];
        }
        //assert(ans>=0);
    }
    return 0;
}

