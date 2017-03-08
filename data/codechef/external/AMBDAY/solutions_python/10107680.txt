#include <bits/stdc++.h>

using namespace std;

#define mem(a, v) memset(a, v, sizeof (a))
#define x first
#define y second
#define all(a) (a).begin(), (a).end()
#define mp make_pair
#define pb push_back
#define sz(x) int((x).size())
#define rep(i, n) for (int i = 0; i < int(n); i ++)
#define repi(i, a, n) for (int i = (a); i < int(n); i ++)
#define repe(x, v) for (auto x: (v))

int main () {
    std::ios_base::sync_with_stdio(false);
    int tst;
    cin >> tst;
    while (tst --) {
        int f, h, w;
        cin >> f >> h >> w;
        vector <int> p(f);
        repe(&x, p) {
            cin >> x;
        }
        int pre = 0, ans = INT_MAX;
        p.pb(w);
        sort(all(p));
        repe(x, p) {
            ans = min(x-pre, ans);
            pre = x;
        }
        cout << 1ll*ans*h << "\n";
    }
    return 0;
}
