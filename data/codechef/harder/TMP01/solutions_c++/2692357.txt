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

const int maxb=20;
const int maxn=1<<maxb;
const int mod=1e9+7;

const int maxN=3*maxn;
const int maxc=26;
const int oo=1e9;

char S[maxn];
struct node{
    map<char,int> next;
    int par,link,l,n;
    void init(){
        next.clear();
        par=link=-1;
        l=n=0;
    }

    int getdeg(){return next.size();}
    void setn(char c, int b){
        next[c]=b;
    }
    int getn(char c){
        if (next.count(c)) return next[c];
        return -1;
    }
    void remn(char c){ next.erase(c); }
};
vector<node> tb;

int where[maxn];
vi avail;


int sz;

int rp,lp;
pii s0;

int tot;
int res;
int rem;

int getn(){
    if (!avail.size()) tb.pb(node()), avail.pb(tb.size()-1);
    int tmp=avail.back(); avail.pop_back();
    tb[tmp].init();
    return tmp;
}

int getr(int nx){return min(nx,rp);}

pii expand(pii sp, int l, int n){
    if (n==0) return sp;
    while(1){

        if (sp.ND==tb[sp.ST].n){
            if (tb[sp.ST].getn(S[l])==-1) return MP(-1,-1);
            sp=MP(tb[sp.ST].getn(S[l]),0);
        }
        node &u=tb[sp.ST];

        if (S[l]!=S[u.l+sp.ND]) return MP(-1,-1);
        int have=u.n-sp.ND;
        if (n<=have) return MP(sp.ST,sp.ND+n);
        l+=have; sp.ND+=have; n-=have;
    }
}

int split(const pii &sp){

    if (sp.ND==0) return tb[sp.ST].par;
    if (sp.ND==tb[sp.ST].n) return sp.ST;

    int id=getn();
    node &u=tb[sp.ST];
    node &nu=tb[id];
    tb[u.par].setn(S[u.l],id);

    nu.par=u.par;
    nu.setn(S[u.l+sp.ND],sp.ST);
    nu.l=u.l; nu.n=sp.ND;

    u.par=id; u.l+=sp.ND; u.n-=sp.ND;

    return id;
}

int find_link(int a){
    if (a==0) return 0;
    if (tb[a].link!=-1) return tb[a].link;
    int p=find_link(tb[a].par);
    pii tmp=expand(MP(p,tb[p].n),tb[a].l+(tb[a].par==0),tb[a].n-(tb[a].par==0));
    int res=split(tmp);
    tb[a].link=res;
    return res;
}

pii find_link2(pii a){
    if (a.ST==0) return MP(0,0);
    int pr=tb[a.ST].par;
    int p=find_link(pr);
    pii tmp=expand(MP(p,tb[p].n),tb[a.ST].l+(pr==0),a.ND-(pr==0));
    assert(tmp.ST!=-1);
    return tmp;
}

void update(char x){
    pii s=s0;
    int prev=-1;

    while(1){
        pii tmp=expand(s,rp-1,1);
        if (tmp.ST!=-1){s=tmp; break;}

        int a=split(s);
        if (tb[a].getn(x)!=-1){ s=MP(tb[a].getn(x),1); break;}

        prev=a;
        int id=getn();
        tb[a].setn(x,id);
        tb[id].l=rp-1; tb[id].n=oo; tb[id].par=a;
        ++tot;

        where[rp-rem]=id;
        --rem;


        int na=find_link(a);
        tb[a].link=na;
        s=MP(na,tb[na].n);
        if (a==0) break;
    }
    s0=s;
}


void add_letter(char x){
    S[rp++]=x;
    ++rem;
    update(x);
    res=(tot+res)%mod;
}

void rem_first(){
    int x=where[lp++];
    int cnt=0;
    --tot;

    int nr=0;
    while(x!=0 && x!=s0.ST && tb[x].getdeg()==0){
        ++nr;
        int px=tb[x].par;
        char cx=S[tb[x].l];

        cnt+=getr(tb[x].l+tb[x].n)-tb[x].l;
        tb[px].remn(cx);
        avail.pb(x);
        x=px;
    }

    if (x && tb[x].getdeg()==0){
        ++tot;
        cnt+=getr(tb[x].l+tb[x].n)-s0.ND-tb[x].l;


        if (s0.ND==0) exit(1);

        //tb[x].n=s0.ND;
        //int u=split(MP(x,s0.ND-1));
        //tb[x].n=oo;
        //tb[x].l=rp-1;
        tb[x].l=rp-s0.ND;
        tb[x].n=oo;
        where[rp-rem]=x;
        --rem;

        s0=find_link2(MP(x,s0.ND));

        //if (u!=0){
        //    pii tmp=expand(s0,rp-1,1);
        //    if (tmp.ST==-1){
        //        nu=nu/0;
        //        tmp=MP(nu,0);
        //    }
        //    s0=tmp;
        //}

    }
    res=(res+mod-cnt)%mod;

}

int count(){ return res; }

void clean(){
    tb.clear();
    avail.clear();
    getn();
    tb[0].n=0; tb[0].l=0; tb[0].par=0; tb[0].link=0;

    rem=0;

    s0=MP(0,0);
    rp=lp=0;

    tot=0;
    res=0;
}

char s[maxn];
int n;
char qq[maxn];
int nq;
char buf[11];

int eval(string s){
    set<string> tb;
    REP(i,s.size()){
        string tmp;
        for (int j=i; j<s.size(); ++j){
            tmp+=s[j];
            tb.insert(tmp);
        }
    }
    return tb.size();
}

int stupid(){
    int l=0, r=0;
    int res=0;

    vi tt;
    REP(i,nq){
        if (qq[i]==-1) ++l;
        else ++r;
        string ss;
        for (int j=l; j<r; ++j) ss+=s[j];

        int xx=eval(ss);
        tt.pb(xx);
        res+=xx;
    }
    //out(tt);

    return res;
}


void gen(){
    nq=50;
    int nx=0;
    int use=1;
    int sz=7;
    int last=0;

    REP(i,nq){
        int x;
        while(1){
            x=rand()%3==0 && use && last>0;

            if (x==0 || nx>1) break;
        }
        if (x==0) qq[i]=s[n++]=rand()%sz+'a', ++nx;
        else qq[i]=-1, --nx, last=0;
        ++last;
    }
    //out(qq,nq);

    //puts("");

}

int main(){
    srand(0);
    int test=0;
    int check=0;

    int res;
start:
    n=0;
    if (!test){
        cin>>nq;
        REP(i,nq){
            scanf("%s",buf);
            if (buf[0]=='+'){
                char x;
                scanf(" %c",&x);
                s[n++]=x;
                qq[i]=x;
            }else qq[i]=-1;
        }
    }else gen();


    res=0;
    clean();
    REP(i,nq){
        if (qq[i]==-1) rem_first();
        else add_letter(qq[i]-'a');
        res=(res+count())%mod;
    }


    if (check){
        int ans=stupid();
        //cout<<s<<endl;
        printf("%d %d\n",ans,res);
        assert(ans==res);
        if (test) goto start;

    }
    printf("%d\n",res);


    return 0;
}

