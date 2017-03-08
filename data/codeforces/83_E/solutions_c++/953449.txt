#include <stdio.h>
#include <string.h>
#include <vector>
using namespace std;
#define rep(i, n) for(int i=0; i<(int)(n); i++)
#define INF (1<<28)
inline void cmin(int &a, int b) { if(a>b) a = b; }

int n, L;
vector<int> dp[21];
char s[32];

int to_i(char *p) {
    int a = 0;
    while(*p) a = a*2+*p++-'0';
    return a;
}

int cover(int a, int b) {
    rep(i, L) if((a&((1<<(L-i))-1))==(b>>i)) return L-i;
    return 0;
}

int main() {
    rep(k, 21) dp[k] = vector<int>(1<<k, INF);
    dp[0][0] = 0;
    scanf("%d %s", &n, s);
    L = strlen(s);
    int pre = to_i(s), base = L;
    rep(_, n-1) {
        scanf(" %s", s);
        const int cur = to_i(s);
        const int t = L - cover(pre, cur);
        base += t;
        int a = INF;
        rep(i, L+1) cmin(a, dp[L-i][cur>>i]+i);
        rep(i, L+1) cmin(dp[i][pre&((1<<i)-1)], a-t);
        pre = cur;
    }
    int ans = INF;
    rep(k, 21) rep(i, 1<<k) cmin(ans, dp[k][i]+base);
    printf("%d\n", ans);
    return 0;
}
