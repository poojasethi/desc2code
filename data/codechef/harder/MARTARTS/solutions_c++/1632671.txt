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


const int maxn=111;
const ll oo=1e15;
const ll oo2=2e18;
struct lx{
    ll a,b;
    lx(){a=b=-oo;}
    lx(ll a, ll b):a(a),b(b){}

    lx operator-(const lx &x)const{return lx(a-x.a,b-x.b);}
    lx operator+(const lx &x)const{return lx(a+x.a,b+x.b);}

    bool operator==(const lx &x)const{return a==x.a&&b==x.b;}
    bool operator<(const lx &x)const{return a!=x.a?a<x.a:b<x.b;}
};

ll a[maxn][maxn];
ll b[maxn][maxn];
ll d[maxn][maxn];

int BLOCK;
lx A[maxn][maxn];
lx u[maxn], v[maxn];

lx sy[maxn];
int idy[maxn];

int par[maxn];
int mx[maxn], my[maxn];


int n;
lx cost;

int q[maxn],na,ne;
int markx[maxn], marky[maxn];

void go(int p){
    na=ne=0;
    q[ne++]=p;


    memset(markx,0,sizeof(markx));
    memset(marky,0,sizeof(marky));

    REP(i,n) sy[i]=lx(oo2,oo), idy[i]=-1;
    do{
        int aa=-1;
        lx dx(oo2,oo);
        while(na<ne){
            int x=q[na++];
            markx[x]=1;
            REP(i,n) if (A[x][i]-u[x]-v[i]<sy[i]) sy[i]=A[x][i]-u[x]-v[i], idy[i]=x;
            REP(i,n) if (!marky[i] && u[x]+v[i]==A[x][i]){
                marky[i]=1;
                par[i]=x;
                if (my[i]==-1){aa=i; goto augment;}
                q[ne++]=my[i];
            }
        }
        REP(i,n) assert(sy[i].a<oo2);

        REP(i,n) if (!marky[i] && sy[i]<dx) dx=sy[i];

        REP(i,n) if (markx[i]) u[i]=u[i]+dx;
        REP(i,n) if (marky[i]) v[i]=v[i]-dx;

        assert(!(dx==lx(0,0)));

        REP(i,n) if (!marky[i]){
            sy[i]=sy[i]-dx;
            if (sy[i]==lx(0,0)){
                assert(idy[i]!=-1);
                par[i]=idy[i];
                marky[i]=1;

                if (my[i]==-1) aa=i;
                else q[ne++]=my[i];
                
            }
        }
        if (aa==-1) continue;
augment:
        assert(aa!=-1);
        while(aa!=-1){
            int na=mx[par[aa]];
            my[aa]=par[aa];
            mx[par[aa]]=aa;
            aa=na;
        }
        return;
    }while(1);

}

int cmp(const pii &x, const pii &y){
    ll da,db; da=d[x.ST][x.ND]; db=d[y.ST][y.ND];
    if (da!=db) return da<db;
    return b[x.ST][x.ND]>b[y.ST][y.ND];
}


lx update(int x, int y, lx c){
    A[x][y]=c;
    u[x]=lx(oo2,oo2);
    REP(j,n) u[x]=min(u[x],A[x][j]-v[j]);
    my[mx[x]]=-1;
    mx[x]=-1;
    go(x);
    cost=lx(0,0);
    REP(i,n) cost=cost+A[i][mx[i]];
    return cost;
}

int main(){
    cin>>n;
    REP(i,n) REP(j,n) scanf(" %Ld:%Ld",a[i]+j,b[i]+j);

    //n=100;
    //REP(i,n) REP(j,n) a[i][j]=rand()%100, b[i][j]=rand()%100;
    //cout<<n<<endl;
    //REP(i,n){ REP(j,n) printf("%Ld:%Ld ",a[i][j],b[i][j]); puts(""); }
    //return 0;


    REP(i,n) REP(j,n) d[i][j]=a[i][j]-b[i][j];

    REP(i,n) REP(j,n) A[i][j]=lx(oo,oo);

    vector<pii> tb;
    REP(i,n) REP(j,n) tb.pb(MP(i,j));
    sort(ALL(tb),cmp);

    cost=lx(0,0);
    REP(i,n) mx[i]=my[i]=i;
    REP(i,n) cost=cost+lx(oo,oo);
    REP(i,n) u[i]=lx(oo,oo);
    REP(i,n) v[i]=lx(0,0);


    lx best=lx(oo2,oo2);
    REP(i,tb.size()){
        int x=tb[i].ST, y=tb[i].ND;
        lx nc=update(x,y,lx(-oo,-oo))+lx(oo,oo);
        update(x,y,lx(-d[x][y],-a[x][y]));

        nc=nc+A[x][y];
        if (d[x][y]>0) nc=nc-A[x][y];
        best=min(best,nc);
    }

    best.a-=best.b;
    printf("%Ld %Ld\n",-best.b,best.a);
    return 0;
}

