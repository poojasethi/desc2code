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

typedef unsigned int uint;
typedef long long int64;
typedef unsigned long long uint64;

using namespace std;

uint next_int() {
    uint res = 0;
    char c = getchar_unlocked();
    while (!isdigit(c))  c = getchar_unlocked();
    while (isdigit(c)) {
        res = 10*res + (c-'0');
        c = getchar_unlocked();
    }
    return res;
}

uint a[10000];
const uint mod = (1<<30)-1;

#define MAXN 500000
int cand[MAXN+1];
int cnt[MAXN+1];

int main(int argc, char* argv[]) {
	
	uint t = next_int();
    while (t--) {
        int N = next_int();
        uint C = next_int();
        int Q = next_int();
        uint A = next_int();
        uint B = next_int();
        uint D = next_int();
        
        REP(i,min(N,10000)) a[i] = next_int();
        
        cand[0] = 0;
        queue<uint> q;
        deque<uint> qmin, qmax;
        
        q.push(a[0]);
        cand[0] = 0;
        qmin.push_back(a[0]);
        qmax.push_back(a[0]);
        
        uint a1 = a[0], a2 = 0;
        int i = 1;
        while (i < N) {
            uint cur = (i<10000) ? a[i] : ((A*a1 + B*a2 + D) & mod);
            a2 = a1; a1 = cur;
            
            q.push(cur);
            while (!qmin.empty() && qmin.back() > cur) qmin.pop_back();
            while (!qmax.empty() && qmax.back() < cur) qmax.pop_back();
            qmin.push_back(cur);
            qmax.push_back(cur);
            
            int j = cand[i-1];
            while (qmax.front()-qmin.front() > C) {
                uint rem = q.front(); q.pop();
                if (rem == qmin.front()) qmin.pop_front();
                if (rem == qmax.front()) qmax.pop_front();
                ++j;
            }
            cand[i] = j;
            ++i;
        }
        
        REP(i,N+1) cnt[i] = 0;
        REP(i,N) cnt[i-cand[i]+1]++;
        cand[N] = cnt[N];
        RFOR(i,N-1,0) cand[i] = cand[i+1] + cnt[i];
        while (Q--) {
            int M = next_int();
            int ans, lo = 1, hi = N;
            while (lo <= hi) {
                int mid = (lo+hi)>>1;
                if (cand[mid] <= M) {
                   ans = mid;
                   hi = mid-1;
                } else {
                    lo = mid+1;
                }
            }
            printf("%d %u\n", ans, cand[ans]);
        }
        
    }
	
	return 0;
}

















