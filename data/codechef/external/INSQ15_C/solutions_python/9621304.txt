#include <bits/stdc++.h>

using namespace std;

typedef unsigned int ui;

const int N = 40;
const int K = (1u<<17);
int v[N], s[N];
int n, k, a, b;
int p[N][K], t[N];
ui res, tot;

int main () {
    scanf("%d %d %d %d", &n, &k, &a, &b);

    for (int i = 0; i < n; i++)
        scanf("%d", v+i);

    for (int i = 0; i < n; i++) {
        s[i] = 1;
        for (int j = 2; j*j <= v[i]; j++) {
            if (v[i]%j == 0)
                s[i] *= j;
            while (v[i]%j == 0)
                v[i] /= j;
        }
        if (v[i] != 1)
            s[i] *= v[i];
    }

    for (ui st = 0; st < (1u<<((n>>1))); st++) {
        int sz = 0;
        int curr = 0;
        for (int i = 0; i < (n>>1); i++)
            if (st&(1u<<i)) {
                curr += s[i];
                sz++;
            }

        if (sz > k) continue;
        p[sz][t[sz]++] = curr;
    }
    tot = (1u<<((k>>1)));
    for (int tm = 0; tm <= k; tm++) {
        sort(p[tm], p[tm]+t[tm]);
 //       printf("%d:", tm);

 //       for (int i = 0; i < t[tm]; i++)
 //           printf(" %d", p[tm][i]);
 //       printf("\n");
    }

    for (ui st = 0; st < (1u<<(((n+1)>>1))); st++) {
        int pr = 0;
        int sz = 0;
        for (int i = 0; i < ((n+1)>>1); i++)
            if (st&(1u<<i)) {
                pr += s[i+(n>>1)];
                sz++;
            }
        if (sz > k)
            continue;

        for (int tm = 0; tm + sz <= k; tm++) {
            res += upper_bound(p[tm], p[tm]+t[tm], b-pr) - p[tm];
            res -= lower_bound(p[tm], p[tm]+t[tm], a-pr) - p[tm];
        }
    }

    printf("%u\n", res);
}
