#include <bits/stdc++.h>
using namespace std;
const int MAXN = 2e3 + 10;

double dp[MAXN][MAXN];
bool visx[MAXN], visy[MAXN];
int n, m, en, em;

int main() {
	int x, y;
	scanf( "%d%d", &n, &m );
	en = em = 0;
	for( int i = 0; i < m; ++i ) {
		scanf( "%d%d", &x, &y );
		if( !visx[x] ) ++en;
		if( !visy[y] ) ++em;
		visx[x] = visy[y] = true;
	}
	dp[n][n] = 0.0;
	for( int i = n; i >= en; --i ) {
		for( int j = n; j >= em; --j ) {
			if( i == n && j == n ) continue;
			double &v = dp[i][j];
			v = ( n - i ) * ( n - j ) * dp[i + 1][j + 1]
				+ ( ( n - i ) * j * dp[i + 1][j] )
				+ ( i * ( n - j ) * dp[i][j + 1] )
				+ 1.0 * n * n;
			v /= 1.0 * n * n - i * j;
		}
	}
	printf( "%.12f\n", dp[en][em] );
	return 0;
}