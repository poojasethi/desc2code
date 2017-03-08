#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <queue>
#include <utility>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define mp make_pair
#define EPS (1e-10)
typedef long long Int;
inline int sq(int a) { return a*a; }

namespace my {

int a, b;
int n, x1[1024], y1[1024], x2[1024], y2[1024];
int vis[1024];

inline int dist(int i, int j) {
    return sq(max(0, max(x1[i], x1[j])-min(x2[i], x2[j])))
           + sq(max(0, max(y1[i], y1[j])-min(y2[i], y2[j])));
}

double solve() {
    priority_queue<pair<double, int> > q;
    q.push(mp(0.0, 0));
    vis[0] = 1;
    double ans = -1;
    while (!q.empty()) {
        const pair<double, int> vv(q.top());
        q.pop();
        const double t = -vv.first;
        const int at = vv.second;
        if (at == 1) return t;
        rep (i, n) if (vis[i] == 0 && dist(at, i) <= a*a) {
            if (i == 1) {
                const double nt = t+sqrt(dist(at, i));
                q.push(mp(-nt, i));
            }
            else {
                vis[i] = 1;
                q.push(mp(-t-a-b, i));
            }
        }
    }
    return ans;
}

int main() {
    scanf("%d%d", &a, &b);
    rep (i, 2) {
        int x, y;
        scanf("%d%d", &x, &y);
        x1[i] = x2[i] = x;
        y1[i] = y2[i] = y;
    }
    scanf("%d", &n);
    rep (i, n) {
        scanf("%d%d%d%d", x1+2+i, y1+2+i, x2+2+i, y2+2+i);
    }
    n += 2;
    rep (i, n) if (x1[i] > x2[i]) swap(x1[i], x2[i]);
    rep (i, n) if (y1[i] > y2[i]) swap(y1[i], y2[i]);
    const double ans = solve();
    if (ans < 0) printf("%d\n", -1);
    else printf("%.9f\n", ans);
    return 0;
}

};

int main() {
    return my::main();
}
