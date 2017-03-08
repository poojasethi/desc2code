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

const int maxn=4000;
const int mod=1e8+7;
const int mod2=2e8+33;

int dp[maxn][maxn][2];
int dp2[maxn][maxn][2];
char s[maxn];

int main(){
    dp[1][0][0]=2;
    FOR(i,1,maxn-1){
        dp[i][0][0]+=dp[i][0][1];
        dp[i][0][1]=0;
        dp[i][0][0]%=mod;
        
        int x=dp[i][0][0];
        dp[i+1][0][0]+=x;
        dp[i+1][1][1]+=x;
        FOR(j,1,i+1){
            int x=dp[i][j][0]; x%=mod;
            dp[i+1][j-1][0]+=x;
            dp[i+1][j][1]+=x;


            x=dp[i][j][1]; x%=mod;
            dp[i+1][j+1][1]+=x;
            dp[i+1][j][0]+=x;
        }
    
    }
    dp2[1][0][0]=2;
    FOR(i,1,maxn-1){
        dp2[i][0][0]+=dp2[i][0][1];
        dp2[i][0][1]=0;
        dp2[i][0][0]%=mod2;
        
        int x=dp2[i][0][0];
        dp2[i+1][0][0]+=x;
        dp2[i+1][1][1]+=x;
        FOR(j,1,i+1){
            int x=dp2[i][j][0]; x%=mod2;
            dp2[i+1][j-1][0]+=x;
            dp2[i+1][j][1]+=x;


            x=dp2[i][j][1]; x%=mod2;
            dp2[i+1][j+1][1]+=x;
            dp2[i+1][j][0]+=x;
        }
    }

    set<pii> h;
    REP(i,maxn) h.insert(MP(dp[i][0][0],dp2[i][0][0]));


    int tn; cin>>tn;
    REP(ti,tn){
        scanf(" %s", s);
        int n=strlen(s);
        int u1=0, u2=0;
        REP(i,n){
            u1=(10*u1+s[i]-'0')%mod;
            u2=(10*u2+s[i]-'0')%mod2;
        }

        if (h.count(MP(u1,u2))) puts("YES");
        else puts("NO");


    }
    return 0;
}

