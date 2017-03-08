#include <stdio.h>
#include <string.h>

int gcd(int a, int b) { return b == 0 ? a : gcd(b, a%b); }

int b, memo[128], vis[128];

int type(int d) {
    if (memo[d]) return memo[d];
    memset(vis, 0, sizeof(vis));
    int x = b%d;
    while (x) {
        if (vis[x]) break;
        vis[x] = 1;
        x = x*b%d;
    }
    if (x == 0) return memo[d] = 2;
    if (b % d == 1) return memo[d] = 3;
    if (b % d == d-1) return memo[d] = 11;
    for (int i = 2; i < d; i++) if (d%i == 0 && gcd(i, d/i) == 1) {
        if (type(i) != 7 && type(d/i) != 7) return memo[d] = 6;
    }
    return memo[d] = 7;
}

int main() {
    int d;
    scanf("%d%d", &b, &d);
    printf("%d-type\n", type(d));
    if (type(d) == 2) {
        int ans = 1, x = b%d;
        while (x) ans++, x = x*b%d;
        printf("%d\n", ans);
    }
    return 0;
}
