#include<stdio.h>

int gcd(int a, int b) {
    if (a == 0) return b;
    if (b == 0) return a;
    return a % b == 0 ? b : gcd(b, a % b);
}

int main()
{
    int t, n, m;
    scanf("%d", &t);
    while (t --) {
        scanf("%d%d", &n, &m);
        printf("%d\n", gcd(n - 1, m - 1) + 1);
    }
    return 0;
}
