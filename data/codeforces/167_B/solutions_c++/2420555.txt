#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int N, M, K;
double g[408][204][204];
double (*f)[204][204] = g+204;
double p[222];
int a[222];

int main() {
	int i, j, k;
	cin>>N>>M>>K;
	f[K][0][0] = 1;
	K = max(N, K);
	for (i = 1; i <= N; ++i) {
		cin>>p[i];
		p[i] /= 100;
	}
	for (i = 1; i <= N; ++i)
		cin>>a[i];
	for (i = 1; i <= N; ++i)
		for (j = 0; j <= N; ++j)
			for (k = -K; k <= K; ++k) {
				f[k+a[i]<=N?k+a[i]:N][i][j+1] += p[i]*f[k][i-1][j];
				f[k][i][j] += (1-p[i])*f[k][i-1][j];
			}
	//printf("%f\n", f[200][1][1]);
	double ans = 0;
	for (j = M; j <= N; ++j)
		for (k = 0; k <= K; ++k)
			ans += f[k][N][j];
	printf("%.10f\n", ans);
	return 0;
}
