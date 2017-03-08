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
#include<stdint.h>
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
typedef uint_fast64_t ull;
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

const ull mod=4294967143LU;
const ull s2=533310557;
const int nb=8;
const int maxm=1<<nb;
const int MASK=maxm-1;
const int maxb=64/nb+1;
int dest[4]={
    0,1,
    1,0,
    };

int prod[4]={
    1,1,
    1,3,
    };

inline void mul(ull *a, ull *b, ull *c){
    c[0]=(a[0]*b[0]%mod+a[1]*b[1]%mod*3)%mod;
    c[1]=a[0]*b[1]%mod+a[1]*b[0]%mod;
    if (c[1]>=mod) c[1]-=mod;
    //REP(i,2){
    //    ull v=a[i];
    //    REP(j,2){
    //        int u=2*i+j;
    //        int d=dest[u];
    //        c[d]=(c[d]+prod[u]*v%mod*b[j]%mod)%mod;
    //    }
    //}
}
inline void add(ull *a, ull *b, ull *c){
    c[0]=a[0]+b[0];
    if (c[0]>=mod) c[0]-=mod;
    c[1]=a[1]+b[1];
    if (c[1]>=mod) c[1]-=mod;
}


ull faste(ull a, ull p=mod-2){ull x=1; for (; p; p>>=1, a=a*a%mod) if (p&1) x=x*a%mod; return x;}

ull XP[5][maxb][maxm][2];
ull ai[5][2], ci[5][2];
ull res, tmp[2], tmp2[2];


int main(){
    int tn; cin>>tn;
    ci[0][0]=7*faste(4)%mod;
    ci[1][0]=11*faste(6)%mod*s2%mod;
    ci[2][1]=23*faste(12)%mod;

    ci[3][0]=(mod-25)*faste(24)%mod*s2%mod;
    ci[3][1]=23*faste(24)%mod*s2%mod;

    ci[4][0]=25*faste(24)%mod*s2%mod;
    ci[4][1]=23*faste(24)%mod*s2%mod;


    ull i2=faste(2);
    ai[0][0]=1;
    ai[1][0]=s2;
    ai[2][1]=1;
    ai[3][0]=(mod-i2)*s2%mod; ai[3][1]=i2*s2%mod;
    ai[4][0]=i2*s2%mod; ai[4][1]=i2*s2%mod;


    REP(i,5){

        REP(j,maxb) XP[i][j][0][0]=1;
        REP(j,maxm-1) mul(XP[i][0][j],ai[i],XP[i][0][j+1]);
        FOR(j,1,maxb){
            mul(XP[i][j-1][maxm-1],XP[i][j-1][1],XP[i][j][1]);
            FOR(k,1,maxm-1) mul(XP[i][j][k],XP[i][j][1],XP[i][j][k+1]);
        }
    }


    REP(ti,tn){
        ull n; scanf(" %Lu",&n);
        --n;
        if (n&1){
            res=0;
            REP(i,5){
                int pw=0;
                ull p=n;

                memset(tmp2,0,sizeof(tmp2));
                tmp2[0]=1;
                while(p){
                    mul(XP[i][pw][p&MASK],tmp2,tmp);
                    REP(j,2) tmp2[j]=tmp[j];
                    ++pw;
                    p>>=nb;
                }

                mul(tmp2,ci[i],tmp);
                res=(res+tmp[0])%mod;
            }
            printf("%Lu\n",res);
        }else printf("0\n");
    }
    return 0;
}

