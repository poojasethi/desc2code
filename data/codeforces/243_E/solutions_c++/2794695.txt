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
#include<unistd.h>
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

const int maxn=555;
int n; 
int a[maxn][maxn], res[maxn][maxn];
int cntb[maxn];
vi e[maxn];
char buf[maxn];
int perm[maxn];
int mark[maxn];

int split(vector<vi> &u, vi &b, vector<vi> &wh, int x){
    int y=b[x];
    swap(b[x],b.back()); b.pop_back();
    vector<vi> nu, nwh;

    
    REP(dir,2){
        int seen=0;
        nu.clear();
        nwh.clear();
        REP(i,u.size()){
            vi xx[2];

            REP(j,u[i].size()){
                int z=u[i][j];
                xx[a[y][z]].pb(z);
            }
            vi &xa=xx[0], &xb=xx[1];


            int pp[2]={nu.size()+1,nu.size()};

            if (!seen && i!=u.size()-1){
                swap(pp[0],pp[1]);
                if (xa.size()) nu.pb(xa);
                if (xb.size()) nu.pb(xb), seen=1;
            }else{
                if (xb.size() && seen==2) goto fail;
                if (xb.size()) nu.pb(xb);
                if (xa.size()) nu.pb(xa), seen=2;
            }
            nwh.resize(nu.size());

            if (xa.size() && xb.size()){
                int p=1;
                if (xa.size()<xb.size()) p=0;
                REP(j,wh[i].size()){
                    int cnt=0;
                    int z=wh[i][j];
                    if (z==y) continue;
                    REP(k,xx[p].size()) cnt+=a[z][xx[p][k]];

                    if (cnt && cnt!=cntb[z]) mark[z]=1;
                    else{
                        if (cnt==cntb[z]) nwh[pp[p]].pb(z);
                        else nwh[pp[p^1]].pb(z);
                    }
                }
            }else if (xa.size() || xb.size()) nwh.back()=wh[i];

            if (i==u.size()-1 && !xa.size()) nwh.pb(vi()), nu.pb(vi());
        }

        u=nu;
        wh=nwh;
        //puts("XXXXXXXXXXXXXXXX");
        //printf("PICKING %d, %d\n",y,u.back().size());
        //REP(i,u.size()) out(u[i]), out(wh[i]), puts("==");
        //out(mark,n);
        //puts("");
        return 1;
fail:
        reverse(u.begin(),u.end()-1);
        reverse(wh.begin(),wh.end()-1);
    }


    return 0;
}


int go(vi &b, vi &in, int pad=0){
    REP(i,b.size()) if (mark[b[i]] || cntb[b[i]]==in.size()) swap(b[i],b.back()), b.pop_back();
    if (!b.size()){
        REP(i,in.size()) perm[in[i]]=pad+i;
        return 1;
    }

    int best=0;
    REP(i,b.size()) if (cntb[b[i]]>cntb[b[best]]) best=i;

    vector<vi> uu; uu.pb(in);
    vector<vi> wh; wh.pb(b);
    mark[b[best]]=1;
    if (!split(uu,b,wh,best)) return 0;

    while(b.size()){
        int cnd=-1;
        REP(i,b.size()) if (mark[b[i]]){cnd=i; break;}
        if (cnd==-1){
            REP(i,uu.size()){
                if (!go(wh[i],uu[i],pad)) return 0;
                pad+=uu[i].size();
            }
            return 1;
        }else{
            if (!split(uu,b,wh,cnd)) return 0;
        }
    }

    REP(i,uu.size()){
        assert(go(wh[i],uu[i],pad));
        pad+=uu[i].size();
    }
    return 1;
}

int main(){
    while(scanf(" %d",&n)>0){
        memset(cntb,0,sizeof(cntb));
        REP(i,n){
            scanf(" %s",buf);
            REP(j,n) a[i][j]=buf[j]-'0';
            REP(j,n) if (a[i][j]) e[i].pb(j), ++cntb[i];
        }

        vi tb; vi in;
        REP(i,n) in.pb(i);
        REP(i,n) if (cntb[i] && cntb[i]<n) tb.pb(i);
        memset(mark,0,sizeof(mark));

        if (go(tb,in)){
            puts("YES");
            REP(i,n) REP(j,n) res[i][perm[j]]=a[i][j];
            REP(i,n){
                REP(j,n) printf("%c",res[i][j]+'0');
                puts("");
            }
        }else puts("NO");
        REP(i,n) e[i].clear();
    }
    return 0;
}

