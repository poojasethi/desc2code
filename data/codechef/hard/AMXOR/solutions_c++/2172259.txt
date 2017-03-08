#include <algorithm>
#include <functional>
#include <vector>
#include <cmath>
#include <cstdio>
#include <cstring>

#define MAX_N 100000
#define MAX_VALUE 1000000000
#define MOD_PRIME 1000000009
#define NUM_BITS 31
#define pow2ll(n) (1LL << (n))

using namespace std;

int v[MAX_N];
int dp[NUM_BITS][NUM_BITS][2];

int get_lower_exp(int n)
{
	int k = -1;
	while (n > 0) {
		k++;
		n >>= 1;
	}
	return k;
}

int addmod(int x, int y)
{
	int sum = x + y;
	if (sum >= MOD_PRIME)
		sum -= MOD_PRIME;
	return sum;
}

int submod(int x, int y)
{
	int diff = x - y;
	if (diff < 0)
		diff += MOD_PRIME;
	return diff;
}

int mulmod(int x, int y)
{
	long long result = x;
	result = (result * y) % MOD_PRIME;
	return (int) result;
}

int invmod(int x)
{
	int result[2][2] = { { 1, 0}, { 0, 1 } };
	int base[2][2] = { { 0, 1}, { 1, 0 } };
	int tmp[2][2];

	int y = x % MOD_PRIME;
	x = MOD_PRIME;
	while (y > 0) {
		int q = x / y;
		int r = x % y;
		base[1][1] = -q;
		memset(tmp, 0, sizeof(tmp));
		for (int i = 0; i < 2; i++)
			for (int j = 0; j < 2; j++) {
				tmp[i][j] = 0;
				for (int k = 0; k < 2; k++)
					tmp[i][j] += result[i][k] * base[k][j];
			}
		memcpy(result, tmp, sizeof(result));
		x = y;
		y = r;
	}
	int inv = result[1][0];
	if (inv < 0)
		inv += MOD_PRIME;
	return inv;
}

int solve_problem()
{
	int n;

	if (scanf("%d", &n) != 1)
		return 1;

	for (int i = 0; i < n; i++)
		if (scanf("%d", &v[i]) != 1)
			return 1;

	sort(v, v + n, greater<int>());
	int result = 0;
	while (v[0] > 0) {
		int nb = get_lower_exp(v[0]);
		int p2nb = 1 << nb;
		int j = 1;
		for (; j < n && nb == get_lower_exp(v[j]); j++) { }

		int parity = j & 1;
		int x[] = { 1, 0 };
		for (int k = 0; k < j; k++) {
			int a = addmod(mulmod(x[0], p2nb), mulmod(x[1], (v[k] - p2nb + 1)));
			int b = addmod(mulmod(x[1], p2nb), mulmod(x[0], (v[k] - p2nb + 1)));
			x[0] = a;
			x[1] = b;
		}

		int y = x[parity];
		int z = 1;
		for (int k = 0; k < j; k++)
			z = mulmod(z, v[k] - p2nb + 1);
		y = submod(y, z);
		y = mulmod(y, invmod(p2nb));
		for (int k = j; k < n; k++)
			y = mulmod(y, v[k] + 1);
		result = addmod(result, y);

		for (int k = 0; k < j; k++)
			v[k] -= p2nb;
		sort(v, v + n, greater<int>());
	}
	result = addmod(result, 1);

	printf("%d\n", result);

	return 0;
}

int main()
{
	int num_tests;

	if (scanf("%d", &num_tests) != 1)
		return 1;
	for (int i = 0; i < num_tests; i++)
		solve_problem();

	return 0;
}
