#include <bits/stdc++.h>

using namespace std;

int main() {
    long long d, h, d0, h0, n, m, ma;

    cin >> n >> m;
    cin >> d >> h;
    ma = h + d - 1;

    for (long int i = 0; i < m; i ++) {
        d0 = d; h0 = h;
        cin >> d >> h;
        if (abs(h - h0) > d - d0) { printf("IMPOSSIBLE\n"); return 0; }
        ma = max(ma, (h + h0 + d - d0) / 2);
    }

    cout << max(ma, h + n - d) << endl;
    return 0;
}
