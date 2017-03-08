#include <bits/stdc++.h>

const int MAXN = 1000001;

int n, k, dp[MAXN], a[MAXN], s[MAXN];

int main() {
	std::cin >> n >> k;
	for (int i = 1; i <= n; i++) {
		std::cin >> a[i];
	}
	int amin = *std::min_element(a + 1, a + n + 1);
	for (int i = 1; i <= n; i++) {
		a[i] -= amin;
		s[i] = std::max(s[i - 1], a[i]);
	}
	for (int i = 1; i <= s[n] * k; i++) dp[i] = ~0u >> 2;
	for (int i = 1; i <= n; i++) {
		for (int j = 0; j <= s[i] * k; j++) {
			if (j >= a[i]) dp[j] = std::min(dp[j], dp[j - a[i]] + 1);
		}
	}
	for (int i = 0; i <= s[n] * k; i++)
		if (dp[i] <= k) {
			//printf("%d %d\n", i, dp[i]);
			std::cout << amin * k + i << " ";
		}
	std::cout << std::endl;
	return 0;
}
