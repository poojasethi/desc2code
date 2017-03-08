#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int N, M, K;
int a[16][128], b[16][128], c[16][128];
char buf[128];

int main() {
    scanf("%d%d%d", &N, &M, &K);
    rep (i, N) {
        scanf(" %s", buf);
        rep (j, M) scanf("%d%d%d", a[i]+j, b[i]+j, c[i]+j);
    }
    int ans = 0;
    rep (i, N) rep (j, N) if (i != j) {
        vector<int> ps;
        rep (k, M) if (a[i][k] < b[j][k]) {
            rep (_, c[i][k]) ps.push_back(b[j][k]-a[i][k]);
        }
        sort(ps.begin(), ps.end());
        reverse(ps.begin(), ps.end());
        if ((int)ps.size() > K) ps.resize(K);
        int s = 0;
        rep (k, ps.size()) s += ps[k];
        ans = max(ans, s);
    }
    printf("%d\n", ans);
    return 0;
}
