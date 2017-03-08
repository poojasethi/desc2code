#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <complex>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <utility>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define mp make_pair
typedef complex<int> P;
#define MOD (1000000007)

int toe(char ch) {
    if (islower(ch)) return ch - 'a';
    else return ch - 'A' + 26;
}

void decode(const char *src, char *dst) {
    int k = 0;
    for (int i = 0; isalpha(src[i]); i++) {
        const int b = toe(src[i]);
        rep (j, 5) dst[k++] = (b&(1<<(4-j))) ? '1' : '0';
    }
}

#define N (1200000)
int n, m;
char buf[500000];
char pat[N], ent[N];
int fail[N], toc[N][2];
int enter;

int to(int k, char ch) {
    while (k >= 0 && pat[k] != ch) k = fail[k];
    return k+1;
}

bool build() {
    int j = fail[0] = -1;
    for (int i = 1; i <= n; i++) {
        while (j >= 0 && pat[j] != pat[i-1]) j = fail[j];
        fail[i] = ++j;
    }
    rep (i, n) rep (k, 2) {
        if (pat[i] == '0' + k) toc[i][k] = i+1;
        else toc[i][k] = fail[i] >= 0 ? toc[fail[i]][k] : 0;
//        assert(toc[i][k] == to(i, '0'+k));
    }
    int k = 0;
    rep (i, m) {
        while (k >= 0 && pat[k] != ent[i]) k = fail[k];
        k++;
        if (k >= n) return true;
    }
    enter = k;
    return false;
}

/*
#define Z (128)
double a[Z][Z];
void eqsolve(int n, double (*a)[Z]) {
    rep(k, n) {
        double mx = -1;
        int ix = -1;
        for(int i=k; i<n; i++) if(mx<fabs(a[i][k])) mx=fabs(a[i][k]), ix=i;
        if(k!=ix) rep(i, n+1) swap(a[k][i], a[ix][i]);
        const double p = a[k][k];
        for(int i=k; i<=n; i++) a[k][i] /= p;
        rep(i, n) if(i!=k) {
            const double d = a[i][k];
            for(int j=k; j<=n; j++) a[i][j] -= d*a[k][j];
        }
    }
}

double solve1() {
    memset(a, 0, sizeof(a));
    rep (i, n) {
        a[i][to(i, '0')] = a[i][to(i, '1')] = -1.0;
        a[i][i] += 2.0;
        a[i][n] = 2.0;
    }
    eqsolve(n, a);
    rep (i, n) printf("a1 [%d] = %f\n", i, a[i][n]);
    return a[enter][n];
}
*/

int b[N], sum[N];

int solve2() {
    rep (i, n) b[i] = 2;
//    memset(sum, 0, sizeof(sum));
    rep (i, n) {
//        const int fr = to(i, pat[i] == '0' ? '1' : '0');
        const int fr = toc[i][pat[i] == '0'];
//        for (int j = fr; j < i; j++) b[i] = (b[i] + b[j]) % MOD;
        //b[i] = (b[i] + sum[i]) % MOD;
        b[i] += sum[i];
        if (b[i] >= MOD) b[i] -= MOD;
        //b[i] = (b[i] + (MOD - sum[fr])) % MOD;
        b[i] += MOD-sum[fr];
        if (b[i] >= MOD) b[i] -= MOD;
        //sum[i+1] = (sum[i] + b[i]) % MOD;
        sum[i+1] = sum[i] + b[i];
        if (sum[i+1] >= MOD) sum[i+1] -= MOD;
    }
    for (int i = n-2; i >= 0; i--) {
        //b[i] = (b[i] + b[i+1]) % MOD;
        b[i] += b[i+1];
        if (b[i] >= MOD) b[i] -= MOD;
    }
//    rep (i, n) printf("a2 [%d] = %d\n", i, b[i]);
    return b[enter];
}

int main() {
    fgets(buf, sizeof(buf), stdin);
    int T = atoi(buf);
    while (T--) {
        char *p;
        fgets(buf, sizeof(buf), stdin);
        n = atoi(buf);
        p = buf;
        while (*p++ != ' ');
        decode(p, pat);
        pat[n] = 0;

        fgets(buf, sizeof(buf), stdin);
        m = atoi(buf);
        p = buf;
        while (*p++ != ' ');
        decode(p, ent);
        ent[m] = 0;

//        printf("%s\n", pat);
//        printf("%s\n", ent);

        if (build()) printf("%d\n", 0);
        else {
//            printf("%f\n", solve1());
            printf("%d\n", solve2());
        }
    }
    return 0;
}
