#include <cstdio>

using namespace std;

int n, m, k;

int main(void) {

    scanf("%d%d%d", &n, &m, &k);

    if (m > n + k){ printf("0\n"); return 0;}

    double sol = 1;
    for (int i = 0; i <= k; ++i) sol *= double (m - i)/(n + k + 1 - i);
    printf("%.8lf\n", (double) 1 - sol);

    return 0;

}
