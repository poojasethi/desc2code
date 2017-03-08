#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
const int maxn = 1e6+5;

int N, M, K, D, L[maxn];
int C[maxn], P[maxn], x[maxn], tmp[maxn];
char str[maxn];

void multi () {
	for (int i = 0; i < N; i++) tmp[i] = x[x[i]];
	for (int i = 0; i < N; i++) x[i] = tmp[i];
}

int main () {
	scanf("%s%d", str, &M);
	N = strlen(str);
	for (int i = 0; i < N; i++)
		L[i] = (i ? i - 1 : N - 1);

	while (M--) {
		scanf("%d%d", &K, &D);

		for (int i = 0; i < N; i++) C[i] = i;
		int mv = 0;
		for (int i = 0; i < D; i++) {
			for (int j = i; j < K; j += D)
				C[j] = mv++;
		}
		for (int i = 0; i < N; i++) P[i] = C[i];
		for (int i = 0; i < N; i++) x[i] = C[L[i]];

		int n = N - K;
		while (n) {
			if (n&1) {
				for (int i = 0; i < N; i++)
					P[i] = x[P[i]];
			}
			multi();
			n >>= 1;
		}
		
		for (int i = 0; i < N; i++) tmp[P[i]] = str[i];
		for (int i = 0; i < N; i++) str[(i + (N - K)) % N] = tmp[i];
		printf("%s\n", str);
	}
	return 0;
}
