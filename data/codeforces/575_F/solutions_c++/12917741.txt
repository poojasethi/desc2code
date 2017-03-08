#include <iostream>
#include <cstdio>
using namespace std;

int n, x;

int main() {
    while (~scanf("%d%d", &n, &x)) {
        int l = x, r = x;
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            int li, ri;
            scanf("%d%d", &li, &ri);

            if (li > r) {
                l = r;
                ans += li - r;
                r = li;
            } else if (ri < l) {
                r = l;
                ans += l - ri;
                l = ri;
            } else {
                l = max(l, li);
                r = min(r, ri);
            }
        }
        printf("%I64d\n", ans);
    }
    return 0;
}
