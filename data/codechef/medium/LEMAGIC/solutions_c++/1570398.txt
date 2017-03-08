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
int A[maxn][maxn];
int n,m;
int dp[maxn][maxn][10][4];
int P;
char buf[maxn];

int go(int a, int b, int c, int f){
    if (a>=n || b>=m) return 0;
    int &r=dp[a][b][c][f];
    if (r!=-1) return r;


    int v=A[a][b];
    if (f&1) v+=P;
    if (f&2) v+=P;
    v%=10;

    REP(xx,2){
        r=max(r,go(a+1,b,c,2*xx+(f&1)));
        r=max(r,go(a,b+1,c,1*xx+(f&2)));
        if (v<=c){
            r=max(r,go(a+1,b,v,2*xx+(f&1))+1);
            r=max(r,go(a,b+1,v,1*xx+(f&2))+1);
        }
    }

    return r;
}

int main(){
    int tn; cin>>tn;
    REP(ti,tn){
        cin>>n>>m;
        REP(i,n){
            scanf(" %s",buf);
            REP(j,m) A[i][j]=buf[j]-'0';
        }
        int res=0;
        FOR(i,1,10){
            P=i;
            memset(dp,-1,sizeof(dp));
            REP(k,4) res=max(res,go(0,0,9,k));
        }
        printf("%d\n",res);

    }

    return 0;
}

