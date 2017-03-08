#include <stdio.h>
#include <string.h>
#include <vector>
using namespace std;
#define rep(i, n) for(int i=0; i<(int)(n); i++)

#define M (100000)
int pt[M];
const int MAX[6] = {0, 9, 99, 999, 9999, 99999};
vector<int> of[6][6][M];
char f[6][6];
int memo[6][1000000];

int rec(int x, int y) {
    if (y == x) {
        return 1;
    }
    int sig = 0;
    rep (i, y) for (int j = y; j < x; j++) sig = sig*10 + f[i][j];
    if (memo[y][sig] != -1) return memo[y][sig];
    int pre = 0;
    rep (i, y) pre = pre*10 + f[i][y];
    int ans = 0;
    rep (k, of[x][y][pre].size()) {
        int p = of[x][y][pre][k];
        rep (i, x) {
            f[y][x-1-i] = p%10;
            p /= 10;
        }
        ans += rec(x, y+1);
    }
    return memo[y][sig] = ans;
}

int main() {
    for (int i = 2; i < M; i++) if (pt[i] == 0) {
        for (int x = 1; x <= 5; x++) {
            if (i > MAX[x]) continue;
            int k = i;
            rep (y, x) {
                of[x][x-y][k].push_back(i);
                k /= 10;
            }
        }
        for (int j = i+i; j < M; j+=i) pt[j] = i;
    }
    int T;
    scanf("%d", &T);
    while (T--) {
        int a;
        scanf("%d", &a);
        int x = 0;
        while (MAX[x] < a) x++;
        rep (i, x) {
            f[0][x-1-i] = a%10;
            a /= 10;
        }
        memset(memo, -1, sizeof(memo));
        printf("%d\n", rec(x, 1));
    }
    return 0;
}
