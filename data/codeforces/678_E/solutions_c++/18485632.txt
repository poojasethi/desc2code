#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

double p[18][18], d[1 << 18][18];

int main()
{
	int n; scanf("%d", &n);
	for(int i = 0; i < n; i++)
		for(int j = 0; j < n; j++) scanf("%lf", &p[i][j]);

	d[1][0] = 1;
	for(int S = 3; S < (1 << n); S++) {
		for(int i = 0; i < n; i++) if(S&(1<<i)) {
			for(int j = 0; j < n; j++) if(j != i && (S&(1<<j))) {
				d[S][i] = max(d[S][i], p[i][j]*d[S^(1<<j)][i] + p[j][i]*d[S^(1<<i)][j]);
			}
		}
	}

	double ans = 0;
	for(int i = 0; i < n; i++) ans = max(ans, d[(1<<n)-1][i]);

	printf("%.15f\n", ans);

	return 0;
}
