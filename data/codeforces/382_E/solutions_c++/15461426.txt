#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

typedef long long lld;

const int maxn = 53, mod = 1e9 + 7;
int n, m;
lld f[maxn][maxn][2], C[maxn][maxn];

void initForComb() {
	C[0][0] = 1ll;
	for(int i = 1; i <= n; i++) {
		C[i][0] = 1ll;
		for(int j = 1; j <= i; j++)
			C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % mod;
	}
//	for(int i = 1; i <= n; i++) {
//		for(int j = 1; j <= i; j++) printf("%lld ", C[i][j]);
//		printf("\n");
//	}
}

void add(lld &a, lld b, lld c, lld d) {
	b *= c; if(b >= mod) b %= mod;
	b *= d; if(b >= mod) b %= mod;
	a += b; if(a >= mod) a -= mod;
}

int main() {
	scanf("%d%d", &n, &m);
	
	if(n <= 1) {
		printf("0\n");
		return 0;
	}
	
	initForComb();
	
	f[1][0][0] = 1; f[0][0][1] = 1;
	for(int i = 2; i <= n; i++) {
		for(int j = 1; j <= i / 2; j++) {
			for(int k1 = 0, k2 = i - 1; k1 <= k2; k1++, k2--) {
				for(int p = 0; p <= j; p++) {
					lld CC;
					if(k1 != k2) CC = C[i - 1][k1] ;
					else CC = C[i - 2][k1 - 1];
					if(k1) CC = CC * k1 % mod * k2 % mod;
					else CC = CC * k2 % mod;
					add(f[i][j][0], f[k1][p][1], f[k2][j - p][1], CC);
					add(f[i][j][1], f[k1][p][1], f[k2][j - p - 1][0], CC);
					add(f[i][j][1], f[k1][p][0], f[k2][j - p - 1][1], CC);
					add(f[i][j][1], f[k1][p][0], f[k2][j - p - 1][0], CC);
				}
			}
//			printf("%d %d %lld %lld\n", i, j, f[i][j][0], f[i][j][1]);
		}
	}
	
	printf("%lld\n", (f[n][m][0] + f[n][m][1]) % mod);
	
	return 0;
}
//btebrajyxtvhpbgyahlqtbldwajktvaleeowlmquvublqzphavhipqtkpcdgymlibrtmhmmroxfqthojyrvuyknxyggxwyxjb