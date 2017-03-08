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

char buf[1111111];
int n, m;
char a[2222222];
int is[2222222][2];



int checkit(int v){
    int p=0, np=1;
    int u=1e8;
    v=-v;
    int v2=2*v;
    ll a=0, d=v;
    for (int i=m-1; i>=0; --i){
        ll ua=a, ud=d;
        ll x;
        a=ud+is[i][0]+v;
        x=ua+is[i][1]+v2;
        if (x>a) a=x;
        
        d=ua+is[i][1]+v;
        x=ud+is[i][0]+v2;
        if (x>d) d=x;
    }
    return a>=0;
}

int doit(){
    REP(i,m) is[i][0]=a[i]=='L'?1e8:0, is[i][1]=a[i]=='R'?1e8:0;
    int H=1e8, T=0;
    int best=0;
    while(T<=H){
        int M=(T+H)/2;
        if (checkit(M)) best=M, T=M+1;
        else H=M-1;
    }
    return best;
}

int main(){
    scanf(" %s", buf);
    n=strlen(buf);
    m=0;
    REP(i,n){
        if (i&&buf[i]!='X'&&buf[i]==buf[i-1]) a[m++]='X';
        a[m++]=buf[i];
    }

    int best=0;
    if (a[0]=='X' || a[0]!=a[m-1]) best=doit();
    else{
        a[m++]='X';
        best=doit();
        REPV(i,m) a[i+1]=a[i];
        a[0]='X';
        checkmax(best,doit());
    }
    printf("%.6lf\n", best/1e6);
    return 0;
}
 

