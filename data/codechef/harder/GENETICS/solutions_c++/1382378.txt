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
const int maxq=33333;

int ca,cb;


struct treap{
    int key;
    int a[4], cnt, type;
    treap *l, *r;
    treap();
    void copy(const treap*);
    void update();
    void get(int);

}tb[maxq*35];

int na;
int res[4];
char buf[33333];
treap *root[maxn];
char rmp[255];
const char *str="AGTC";


inline int count(const treap *a){return a?a->cnt:0;}

void treap::copy(const treap *b){
        REP(i,4) a[i]=b->a[i];
        cnt=b->cnt;
        type=b->type;
        l=b->l; r=b->r;
    }

treap::treap(){key=rand(); memset(a,0,sizeof(a)); cnt=1; l=r=0; type=0;}

void treap::update(){
    cnt=1+count(l)+count(r);
    REP(i,4) a[i]=0;
    a[type]=1;
    if (l) REP(i,4) a[i]+=l->a[i];
    if (r) REP(i,4) a[i]+=r->a[i];
}
void treap::get(int x){
    int na=count(l);
    if (na>x) l->get(x);
    else{
        if (l) REP(i,4) res[i]+=l->a[i];
        if (na<x) ++res[type];
        if (x-na>1) r->get(x-na-1);
    }
}


treap *merge0(treap *a, treap *b){
    if (!a) return b;
    if (!b) return a;
    if (a->key<b->key){
        a->r=merge0(a->r,b);
        a->update();
        return a;
    }
    b->l=merge0(a,b->l);
    b->update();
    return b;
}

treap *merge(treap *a, treap *b){
    if (!a) return b;
    if (!b) return a;
    if (a->key<b->key){
        treap *u=tb+na++;
        u->copy(a);
        u->r=merge(u->r,b);
        u->update();
        return u;
    }
    treap *u=tb+na++;
    u->copy(b);
    u->l=merge(a,u->l);
    u->update();
    return u;
}
treap *split(treap *a, treap *&b, int x){
    //    if (!x){b=a; return 0;}
    //    if (x>a->cnt){b=0; return a;}
    if (!a){b=0; return 0;}
    treap *res;
    treap *u=tb+na++;
    u->copy(a);
    int cl=count(u->l);
    if (x<=cl) res=split(u->l,u->l,x),b=u;
    else u->r=split(u->r,b,x-cl-1), res=u;
    u->update();
    return res;
}

treap *chang(treap *a, int x){
    treap *u=tb+na++;
    u->copy(a);
    ++u->a[cb];
    int cl=count(u->l);
    if (cl>=x) u->l=chang(u->l,x);
    else if (x-cl>1) u->r=chang(u->r,x-cl-1);
    else ca=u->type, u->type=cb;
    --u->a[ca];
    return u;
}



int main(){
    int n; cin>>n;
    REP(i,4) rmp[str[i]]=i;

    na=1;
    REP(i,n){
        scanf(" %s",buf);
        int nx=strlen(buf);
        treap *r=0;
        REP(j,nx){
            treap *a=tb+na++;
            a->type=rmp[buf[j]];
            a->a[a->type]=1;
            r=merge0(r,a);
        }
        root[i+1]=r;
    }
    ++n;

    int nq; cin>>nq;
    REP(step,nq){
        scanf(" %s",buf);
        if (buf[1]=='O'){
            int a,b,c; scanf(" %d%d%d",&a,&b,&c);
            REP(i,4) res[i]=0;
            if (root[a]){
                c=min(c,root[a]->cnt);
                if (b-1) root[a]->get(b-1);
                REP(i,4) res[i]=-res[i];
                root[a]->get(c);
            }
            REP(i,4) printf("%d ",res[i]); puts("");
        }else if (buf[1]=='U'){
            int a,b; char c;
            scanf(" %d%d %c",&a,&b,&c);
            cb=rmp[c];
            root[a]=chang(root[a],b);
        }else{
            int a,b,c,d; scanf(" %d%d%d%d",&a,&b,&c,&d);
            treap *u,*nu,*v,*nv;
            u=split(root[a],nu,c);
            v=split(root[b],nv,d);
            root[n++]=merge(u,nv);
            root[n++]=merge(v,nu);
        }
    }

    return 0;
}


