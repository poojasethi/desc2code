#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <stack>
#include <algorithm>
#include <cctype>
#include <vector>
#include <queue>
#include <tr1/unordered_map>
#include <cmath>
#include <map>
#include <bitset>
#include <set>
#include <iomanip>
#include <cstring>
#include <unistd.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector< ii > vii;
///////////////////////////////UTIL/////////////////////////////////
#define ALL(x) (x).begin(),x.end()
#define CLEAR0(v) memset(v, 0, sizeof(v))
#define CLEAR(v, x) memset(v, x, sizeof(v))
#define COPY(a, b) memcpy(a, b, sizeof(a))
#define CMP(a, b) memcmp(a, b, sizeof(a))
#define REP(i,n) for(int i = 0; i<n; i++)
#define REPP(i,a,n) for(int i = a; i<n; i++)
#define REPD(i,n) for(int i = n-1; i>-1; i--)
#define REPDP(i,a,n) for(int i = n-1; i>=a; i--)
#define pb push_back
#define pf push_front
#define sz size()
#define mp make_pair
/////////////////////////////NUMERICAL//////////////////////////////
#define INF 0x3f3f3f3f
/////////////////////////////BITWISE////////////////////////////////
#define CHECK(S, j) (S & (1 << j))
#define CHECKFIRST(S) (S & (-S)) 
#define SET(S, j) S |= (1 << j)
#define SETALL(S, j) S = (1 << j)-1  
#define UNSET(S, j) S &= ~(1 << j)
#define TOOGLE(S, j) S ^= (1 << j)
///////////////////////////////64 BITS//////////////////////////////
#define LCHECK(S, j) (S & (1ULL << j))
#define LSET(S, j) S |= (1ULL << j)
#define LSETALL(S, j) S = (1ULL << j)-1ULL 
#define LUNSET(S, j) S &= ~(1ULL << j)
#define LTOOGLE(S, j) S ^= (1ULL << j)
#define EPS 10e-20
#define MOD 1000000007
//__builtin_popcount(m)
//scanf(" %d ", &t);
 
int n, m;
vi g[410];
int mate[410];
bitset<410> vis;

bool aug(int v){
    if(vis[v]) return false;
    vis[v] = true;
    REP(i, g[v].size()){
        int w = g[v][i];
        if(mate[w] == -INF || aug(mate[w])){
            mate[w] = v;
            return true;
        }
    }
    return false;
}

int MCBM(){
    REP(i, 2*n+1) mate[i] = -INF; 
    int mcbm = 0;
    REPP(i, 1, n+1){
        vis.reset();
        mcbm += aug(i);
    }
    return mcbm;
}

int main(){
	scanf(" %d %d ", &n, &m);
	int u, v;
	REP(i, m){
		cin >> u >> v; 
		g[u].push_back(v+n);
		g[v+n].push_back(u);
		g[u+n].push_back(v);
		g[v].push_back(u+n);
	}
	int ans = n - MCBM();
	printf("%d\n", ans);
	
}
