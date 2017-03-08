#include <cstdio>
#include <cstring>

const int N = 1e5+5;

int n, jump[N], c, r[N], dp[N];
char str[N];

void getJump() {
	int k = 0;
	n = strlen(str+1);
	for (int i = 2; i <= n; i++) {
		while (k && str[i] != str[k+1])
			k = jump[k];

		if (str[i] == str[k+1])
			k++;
		jump[i] = k;
	}
}

int main () {
	scanf("%s", str+1);
	getJump();

	c = 0;
	for (int i = jump[n]; i; i = jump[i]) {
		r[c] = i;
		c++;
	}

	memset(dp, 0, sizeof(dp));
	for (int i = n; i; i--) {
		dp[i]++;
		dp[jump[i]] += dp[i];
	}

	printf("%d\n", c+1);
	for (int i = c-1; i >= 0; i--)
		printf("%d %d\n", r[i], dp[r[i]]);
	printf("%d %d\n", n, dp[n]);
	return 0;
}
