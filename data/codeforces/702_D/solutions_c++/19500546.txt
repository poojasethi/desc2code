#include <bits/stdc++.h>
#define INF 1e18
using namespace std;

long long d, k, a, b, t;

int main() {
    cin >> d >> k >> a >> b >> t;
    long long ans = 0;
    if (d <= k) ans = d * a;
    else if (t + k * a > k * b) ans = k * a + (d - k) * b;
    else ans = (d / k) * k * a + (d / k - 1) * t + min(t + (d % k) * a, (d % k) * b);
    cout << ans << endl;
    return 0;
}
