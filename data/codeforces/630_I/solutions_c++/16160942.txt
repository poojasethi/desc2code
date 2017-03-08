#include <cstdio>

int main() {
	int n;
	scanf("%d", &n);
	unsigned long long ans = 0;
	ans += 4 * 3 * (1ull << (n - 3) * 2) * 2;
	ans += 3 * 4 * 3 * (1ull << (n - 4) * 2) * (n - 3);
	printf("%I64u\n", ans);
	return 0;
}
