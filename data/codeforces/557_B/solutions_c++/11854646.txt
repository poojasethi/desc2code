#include <cstdio>
#include <algorithm>

const int N = 1000000 + 10;

int n, w, a[N];

int main()
{
	scanf("%d%d", &n, &w);
	for(int i = 1; i <= 2 * n; i++) scanf("%d", &a[i]);
	std::sort(a+1, a+1+n+n);
	double x = std::min(a[1] * 1.0, a[n+1]/2.0);
	printf("%f\n", std::min(w + 0.0, 3 * n * x));
	return 0;
}
