#include <bits/stdc++.h>
#define pb push_back
#define ms(a, b) memset((a), b, sizeof(a))
#define MOD 1000000007

using namespace std;

int main() {
	long long n, k, ans = 1, A, K = 1;
	cin >> n >> k;
	long long ndk = n/k, a[ndk], b[ndk], part;
	for (int i = 0; i < ndk; i++)
		cin >> a[i];
	for (int i = 0; i < ndk; i++)
		cin >> b[i];
	for (int i = 0; i < k - 1; i++)
		K *= 10;
	for (int i = 0; i < ndk; i++) {
		part = (10*K - 1)/a[i];
		if (b[i])
			part -= ( ((b[i] + 1)*K - 1)/a[i] - (b[i]*K - 1)/a[i] ) - 1;
		else
			part -= (K-1)/a[i];
		ans *= part;
		ans %= MOD;
	}
	cout << ans << endl;
	return 0;
}