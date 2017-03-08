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

const int maxn=1e6+10;
const int mod=1e9+7;
int n, m;
char sa[maxn], sb[maxn];
int ta[maxn], tb[maxn];
int p[maxn], p2[maxn], p3[maxn];

int dpa[maxn], dpb[maxn];

int faste(int a, int p){int x=1; for (; p; p>>=1, a=1ll*a*a%mod) if (p&1) x=1ll*x*a%mod; return x;}



int main(){
    int tn; cin>>tn;
    REP(ti,tn){
        scanf("%d %s", &n,sa);
        char c;
        for (int i=0; i<n; ++i){
            if (i%5==0){
                c=sa[i/5];
                if (c>='a') c-='a';
                else c-='A'-26;
            }
            ta[i]=c>>(4-i%5)&1;
        }
        scanf("%d %s", &m,sb);
        for (int i=0; i<m; ++i){
            if (i%5==0){
                c=sb[i/5];
                if (c>='a') c-='a';
                else c-='A'-26;
            }
            tb[i]=c>>(4-i%5)&1;
        }

        p[0]=-1;
        FOR(i,0,n){
            int px=p[i];
            while(px>=0 && ta[px]!=ta[i]) px=p[px];
            p[i+1]=px+1;
        }

        REP(i,n){
            int px=p[i];
            while(px>=0 && ta[px]==ta[i]) px=p[px];
            p3[i]=px+1;
        }

        REP(i,m){
            int px=p2[i];
            while(px>=0 && ta[px]!=tb[i]) px=p[px];
            p2[i+1]=px+1;
        }
        int fd=0;
        REP(i,m+1) if (p2[i]==n){fd=1; puts("0");break;}
        if (fd) continue;

        dpa[0]=1;
        REP(a,n){
            int u=p3[a];

            int x=(2*dpa[a]-dpa[u])%mod;
            while(x>=mod) x-=mod;
            while(x<0) x+=mod;
            dpa[a+1]=x;

            x=(2*dpb[a]-dpb[u]-2)%mod;
            while(x>=mod) x-=mod;
            while(x<0) x+=mod;
            dpb[a+1]=x;
        }

        int eo=1ll*(mod-dpb[n])*faste(dpa[n],mod-2)%mod;
        int u=p2[m];
        int res=(1ll*dpa[u]*eo+dpb[u])%mod;
        printf("%d\n",res);
    }
    return 0;
}

