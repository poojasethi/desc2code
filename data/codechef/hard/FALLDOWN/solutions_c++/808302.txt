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

const int maxn=2048;

int mp[maxn][maxn];
int dp[2][maxn];
int A[maxn], B[maxn];


int main(){
    int tn; cin>>tn;
    REP(ti, tn){
        int r, c, type;
        cin>>r>>c>>type;
        memset(mp, 0, sizeof(mp));
        if (type==1){
            REP(i, r) REP(j, c) scanf(" %d", &mp[i][j]);
        }else{
            int x, m, p, q;
            cin>>x>>p>>q>>m;
            int cur=x;
            REP(i, r) REP(j, c) cur=(cur*p+q)%m, mp[i][j]=x-cur;
        }
        int p=0, np=1;
        REP(i, c) dp[p][i]=0;
        REP(i, r){
            int u, v;
            v=u=INT_MIN+555;
            A[0]=0; REP(j,c-1) A[j+1]=max(0,A[j]+mp[i][j]);
            A[c-1]=0; for (int j=c-1; j; --j) B[j-1]=max(0,B[j]+mp[i][j]);


            REP(j, c){
                u=max(u, 0)+mp[i][j];
                v=max(v+mp[i][j], u+dp[p][j]);
                dp[np][j]=v+B[j];
            }
            v=u=INT_MIN+555;
            REPV(j, c){
                u=max(u, 0)+mp[i][j];
                v=max(v+mp[i][j], u+dp[p][j]);
                checkmax(dp[np][j], v+A[j]);
            }

            p=np; np^=1;
        }
        
        int res=INT_MIN;
        REP(i, c) checkmax(res, dp[p][i]);
        printf("%d\n", res);
        
    }
    return 0;

}

