#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<cctype>
#include<algorithm>

using namespace std;

const int MaxN = 1000000 + 5;

int N, L, T;
unsigned a[MaxN * 2];
double ans;

int main() {

    scanf("%d%d%d", &N, &L, &T); 
    L *= 2; T *= 2;
    ans = 0.5 * (T / (L / 2)) * N * (N - 1) / 2;
    T %= (L / 2);
    for (int i = 0; i < N; ++i) {
        scanf("%d", a + i);
        a[i] *= 2;
        a[i + N] = a[i] + L;
    }
    for (int i = 0; i < N; ++i) {
        ans += 0.25 * (upper_bound(a, a + 2 * N, a[i] + T * 2) - a - i - 1);
    }
    printf("%.9f\n", ans);

    return 0;

}
