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

#define FILL(X, V) memset( X, V, sizeof(X) )
#define TI(X) __typeof((X).begin())
#define ALL(V) V.begin(), V.end()
#define SIZE(V) int((V).size())

#define FOR(i, a, b) for(int i = a; i <= b; ++i)
#define RFOR(i, b, a) for(int i = b; i >= a; --i)
#define REP(i, N) for(int i = 0; i < N; ++i)
#define RREP(i, N) for(int i = N-1; i >= 0; --i)
#define FORIT(i, a) for( TI(a) i = a.begin(); i != a.end(); i++ )

#define PB push_back
#define MP make_pair

template<typename T> T inline SQR( const T &a ){ return a*a; }
template<typename T> T inline ABS( const T &a ){ return a < 0 ? -a : a; }
template<typename T> T inline MIN( const T& a, const T& b){ if( a < b ) return a; return b; }
template<typename T> T inline MAX( const T& a, const T& b){ if( a > b ) return a; return b; }

const double EPS = 1e-9;
inline int SGN( double a ){ return ((a > EPS) ? (1) : ((a < -EPS) ? (-1) : (0))); }
inline int CMP( double a, double b ){ return SGN(a - b); }

typedef long long int64;
typedef unsigned long long uint64;

using namespace std;

struct edge_t {
	int v, c;
	edge_t( int vv = 0, int cc = 0 ) : v(vv), c(cc) {}
};


#define MAXN 65536

int64 D[MAXN+2];

int seen[MAXN+1];
vector< vector< edge_t > > gr;

bool dfs( int u, int acum = 0 ){
	
	int sz = SIZE(gr[u]);
	seen[u] = 1;
	
	REP( i, sz ){
		int v = gr[u][i].v;
		if( !seen[v] ){
			D[v] = D[u]+gr[u][i].c;
			if( dfs( v ) ) return true;
		} else if( D[v] != D[u] + gr[u][i].c ) return true;
	}
	
	return false;
}

int main( int argc, char* argv[] ){

	ios::sync_with_stdio(false);
	
	int N, M;
	cin >> N >> M;
	gr.resize(N+1);
	
	REP( i, N+1 ){ seen[i] = 0; }
	
	int x, y, z;
	while( M-- ){
		cin >> x >> y >> z;
		gr[x-1].PB( edge_t( y, z ) );
		gr[y].PB( edge_t( x-1, -z ) );
	}
	
	bool cycle = false;
	REP( i, N+1 ) if( !seen[i] ){
		D[i] = (i?D[i-1]:0);
		cycle = dfs(i);
		if( cycle ) break;
	}
	
	if( cycle ) puts("-1");
	else {
		
		FOR( i, 1, N ){ 
			if( i-1 ) cout << ' ';
			cout <<  D[i]-D[i-1];
		}
		cout << "\n";

	}
	
	return 0;
}








