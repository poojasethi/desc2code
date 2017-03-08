#include <map> 
#include <set> 
#include <list>
#include <stack>
#include <cmath> 
#include <queue> 
#include <ctime>
#include <cfloat>
#include <vector> 
#include <string> 
#include <cstdio>
#include <bitset>
#include <climits> 
#include <cstdlib> 
#include <cstring> 
#include <cassert> 
#include <iomanip>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>

#define INF 0x3F3F3F3F
#define LINF 0x3F3F3F3FFFFFFFFFLL

#define FILL(X, V) memset(X, V, sizeof(X))
#define TI(X) __typeof((X).begin())
#define ALL(V) V.begin(), V.end()
#define SIZE(V) int((V).size())

#define FOR(i, a, b) for(int i = a; i <= b; ++i)
#define RFOR(i, b, a) for(int i = b; i >= a; --i)
#define REP(i, N) for(int i = 0; i < N; ++i)
#define RREP(i, N) for(int i = N-1; i >= 0; --i)
#define FORIT(i, a) for(TI(a) i = a.begin(); i != a.end(); i++)

#define PB push_back
#define MP make_pair

template<typename T> T inline SQR(const T &a) { return a*a; }
template<typename T> T inline ABS(const T &a) { return a < 0 ? -a : a; }

const double EPS = 1e-9;
inline int SGN(double a){ return ((a > EPS) ? (1) : ((a < -EPS) ? (-1) : (0))); }
inline int CMP(double a, double b){ return SGN(a - b); }

typedef long long int64;
typedef unsigned long long uint64;

using namespace std;

int d1[][2] = {{-1,0}, {0,-1}, {-1,0}, {0,+1}, {+1,0}, {0,-1}};
int d2[][2] = {{+1,0}, {0,+1}, {0,+1}, {+1,0}, {0,-1}, {-1,0}};
int p1[6], p2[6];    

int64 chng[35][35][6];
int64 cros[35][35];

int popc(int64 x) {
    int res = 0;
    while (x > 0LL) {
        res++;
        x -= (x & -x);
    }
    return res;
}

#define MAXGUESS 325000
int64 C[MAXGUESS];
    
int main(int argc, char* argv[]) {
	
	ios::sync_with_stdio(false);
	
	int N, M, Q;
    cin >> N >> M >> Q;
    
    int sx, sy;
    cin >> sx >> sy;
    sx--, sy--;
    
    REP(i,6) cin >> p1[i] >> p2[i];
    
    REP(i,N) REP(j,M) {
        cros[i][j] = 0;
        
        REP(ii,N) cros[i][j] |= (1LL << (ii*M + j));
        REP(jj,M) cros[i][j] |= (1LL << (i*M + jj));
                        
        REP(k, 6) {
            chng[i][j][k] = 0;
            
            int ii = i + d1[k][0]*p1[k];
            int jj = j + d1[k][1]*p1[k];
            
            while (0 <= ii && ii < N && 0 <= jj && jj < M) {   
                chng[i][j][k] |= (1LL << (ii*M + jj));
                ii += d1[k][0]*p1[k];
                jj += d1[k][1]*p1[k];
            }
            
            ii = i + d2[k][0]*p2[k];
            jj = j + d2[k][1]*p2[k];
            
            while (0 <= ii && ii < N && 0 <= jj && jj < M) {   
                chng[i][j][k] |= (1LL << (ii*M + jj));
                ii += d2[k][0]*p2[k];
                jj += d2[k][1]*p2[k];
            }              
        }
    }
    
    int64 init = 0;
    init |= (1LL << (sx*M + sy));
    
    map<int64, int> seen;
    seen[init] = 0;
    int t = 0;
    C[0] = 1;
    int p, q;
    
    while (true) {
        
        int64 next = init;
        
        REP(i,N) REP(j,M) {
            if (init & (1LL << (i*M + j))) {
                int have = popc(init & cros[i][j]) % 6;
                next ^= chng[i][j][have];
            }
        }
                
        init = next;
        if (seen.count(init)) {
            p = t+1;
            q = seen[init];
            break;
        }
        ++t;
        C[t] = C[t-1] + popc(init);
        seen[init] = t;
    }
    int len = p - q;
        
    while (Q--) {
       int64 T;
       cin >> T;
       if (T < p) cout << C[T] << "\n";
       else {
           int64 res = q ? C[q-1] : 0;
           int64 per = (p ? C[p-1] : 0) - (q ? C[q-1] : 0);
           res += per * int64((T-q+1LL) / len);
           int rem = (T-q+1) % len;
           res += ((q+rem >= 1) ? C[q+rem-1] : 0) - (q ? C[q-1] : 0);
           cout << res << "\n";
       }
    }
    
	return 0;
}

















